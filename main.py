from qtpy.QtCore import *
from qtpy.QtWidgets import *
from qtpy.QtGui import *
from qtpy import uic
import sys
import os
from odbcAccess import *
from matplotlib.backends.backend_qt5agg import FigureCanvas as Canvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavTB
from matplotlib.figure import Figure
from myNavigation import *
import icons
import json
from functools import partial
import numpy as np
from saveToDat import saveDAT
from data_source_lib import *
#import os
#from shutil import copyfile
from raySelectionDialog import *
import numpy.fft as fftt
from reportLib import *
import xlwt
from syncDialog import MySyncDialog
from dispersionLib import barWithDispersion

def copyAction(action):
    if not action.parent():
        parent=None
    else:
        parent=action.parent()
    newA=QAction(parent)
    newA.setIcon(action.icon())
    newA.setText(action.text())
    newA.setCheckable(action.isCheckable())
    return newA

def movingAverage2(data,degree=10):  
    smoothed=np.zeros(len(data)-degree+1)
    for i in range(len(smoothed)):
        smoothed[i]=sum(data[i:i+degree])/degree
    return smoothed

def movingAverage(x, N=10):
    rez = np.roll(np.convolve(x, np.ones((N,))/N)[(N-1):], N//2)
    rez[:N//2] = rez[N//2]
    return rez

def fft_filter(maxtime, data, freq):
    numpoints = int(np.floor(freq*maxtime))
    y1=fftt.rfft(data)
    if numpoints and numpoints<len(data):
        rez = [0]*len(y1)
        rez[0:numpoints]=y1[0:numpoints]
    return fftt.irfft(rez) 

class MatplotlibWidget(Canvas):
    def __init__(self, parent=None):
        figure = Figure(figsize=(4,3))
        self.ax = figure.add_subplot(111)
        Canvas.__init__(self, figure)
        c=Canvas(Figure())
        self.setParent(parent)
        Canvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
        self.figure=figure
        self.ax.grid()
        self.tb=NavTB(self.figure.canvas, self)
        self.tb.hide()
        self.nav = MyNavigation(self.ax, mplwidget=self)
#        self.ax.set_xlabel('время, мкс')
        self.figure.subplots_adjust(right=0.98, top=0.98)

class MyWindow(QMainWindow):
#    def eventFilter(self, obj, ev):
#        if ev.type()==QEvent.KeyPress:
#            print(ev.key())
#            return True
#        return False
    def scAction(self, direction):
        if self.tabWidget.currentIndex()!=3: return
        l=self.mplPulses.ax.get_lines()
        if len(l)<4: return
        dy=1e-5
        mult=1.0 if direction=='up' else -1.0
        l[2].set_ydata(l[2].get_ydata()+mult*self.trDy)
        self.mplPulses.figure.canvas.draw_idle()
        
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('main.ui', self)
        self.radioButtons=[]
        for gb in [self.gbX, self.gbY1, self.gbY2]:
            b1 = QRadioButton("t")
            b2 = QRadioButton("e")
            b3 = QRadioButton("s")
            b4 = QRadioButton("de")
            gb.layout().addWidget(b1)
            gb.layout().addWidget(b2)
            gb.layout().addWidget(b3)
            gb.layout().addWidget(b4)
            self.radioButtons.append([b1, b2, b3, b4])
        self.radioButtons[0][1].setChecked(True)
        self.radioButtons[1][2].setChecked(True)
        self.radioButtons[2][3].setChecked(True)
        b = QRadioButton("None")
        self.gbY2.layout().addWidget(b)
        self.radioButtons[2].append(b)

#       Matplotlib widgets
        self.mplOsc = MatplotlibWidget(self)
        self.mplLayout.addWidget(self.mplOsc)
        self.mplPulses = MatplotlibWidget(self)
        self.vlPulses.addWidget(self.mplPulses)
        self.mplDiagramm = MatplotlibWidget(self)
        self.vlDiagramm.addWidget(self.mplDiagramm)
        self.mplComparDiag = MatplotlibWidget(self)
        self.vlComparDiag.addWidget(self.mplComparDiag)      
        self.mpls=[None, self.mplOsc, None, self.mplPulses, self.mplDiagramm, self.mplComparDiag]
#        self.tabWidget.installEventFilter(self)
        self.scUP=QShortcut(QKeySequence('CTRL+UP'), self)
        self.scDOWN=QShortcut(QKeySequence('CTRL+DOWN'), self)
        self.scUP.activated.connect(partial(self.scAction, 'up'))
        self.scDOWN.activated.connect(partial(self.scAction, 'down'))

        self.toolBars=[]
        for i in range(self.tabWidget.count()):
            self.toolBars.append(self.addToolBar('tb{}'.format(i+1)))
            self.toolBars[i].setVisible(False)

        self.toolBars[0].addAction(self.actionSaveToDat)
        self.toolBars[0].addAction(self.actionUpdateODBCContent)
        self.toolBars[0].setVisible(True)
#        self.toolBars[0].addSeparator()
        self.toolBars[0].addAction(self.actionReadData)

#	Osc tab tool bar setup

        self.toolBars[1].addAction(self.actionMplHome)

        self.oscNavModeAG=QActionGroup(self.mplOsc)
        self.oscNavZoomMode=copyAction(self.actionZoom)
        self.oscNavZoomMode.setData('zoom')
        self.oscNavModeAG.addAction(self.oscNavZoomMode)
        self.toolBars[1].addAction(self.oscNavZoomMode)

        self.oscNavPanMode=copyAction(self.actionPan)
        self.oscNavPanMode.setData('pan')
        self.oscNavModeAG.addAction(self.oscNavPanMode)
        self.toolBars[1].addAction(self.oscNavPanMode)

        self.oscNavIntervalMode=copyAction(self.actionInterval)
        self.oscNavIntervalMode.setData('interval')
        self.oscNavModeAG.addAction(self.oscNavIntervalMode)
        self.toolBars[1].addAction(self.oscNavIntervalMode)
        self.toolBars[1].addSeparator()
        self.oscNavModeAG.triggered.connect(self.setMode)

        self.toolBars[1].addAction(self.actionCut)
        self.toolBars[1].addAction(self.actionZero)
        self.toolBars[1].addAction(self.actionSmooth)
        self.toolBars[1].addAction(self.actionReduceData)
#        self.toolBars[1].addAction(self.actionScaleRays)
        self.toolBars[1].addSeparator()
        self.toolBars[1].addAction(self.actionPlotCurve)
        self.toolBars[1].addAction(self.actionPolyFit)
        self.actionPlotCurve.setParent(self.mplOsc)
        self.actionPlotCurve.setData('curve')
        self.actionPlotCurve.setCheckable(True)
        self.oscNavModeAG.addAction(self.actionPlotCurve)
        self.toolBars[1].addAction(self.actionApplyCurve)
        self.toolBars[1].addAction(self.actionDeleteLine)
        self.toolBars[1].addAction(self.actionCompressCurve)
        self.toolBars[1].addSeparator()
        self.toolBars[1].addAction(self.actionOpenOSC)
        self.toolBars[1].addAction(self.actionSaveOSC)
        self.getRayFromExperiment=QAction(parent=self, text='GetRay')
        self.toolBars[1].addSeparator()
        self.toolBars[1].addAction(self.getRayFromExperiment)
        self.getRayFromExperiment.triggered.connect(self.getRayFromExperiment_triggered)
#       tab 1 end

#       tab 3
        self.toolBars[3].addAction(self.actionMplHome)

        self.plssNavModeAG=QActionGroup(self.mplPulses)
        self.plssNavZoomMode=copyAction(self.actionZoom)
        self.plssNavZoomMode.setData('zoom')
        self.plssNavModeAG.addAction(self.plssNavZoomMode)
        self.toolBars[3].addAction(self.plssNavZoomMode)

        self.plssNavPanMode=copyAction(self.actionPan)
        self.plssNavPanMode.setData('pan')
        self.plssNavModeAG.addAction(self.plssNavPanMode)
        self.toolBars[3].addAction(self.plssNavPanMode)

        self.plssNavIntervalMode=copyAction(self.actionInterval)
        self.plssNavIntervalMode.setData('interval')
        self.plssNavModeAG.addAction(self.plssNavIntervalMode)
        self.toolBars[3].addAction(self.plssNavIntervalMode)
        self.toolBars[3].addSeparator()
        self.plssNavModeAG.triggered.connect(self.setMode)
        self.toolBars[3].addSeparator()

        self.toolBars[3].addAction(self.actionCut)
        self.toolBars[3].addSeparator()

        self.toolBars[3].addAction(self.actionSavePulses)
        self.toolBars[3].addAction(self.actionSyncPulses)
        self.actionSmoothPulses = copyAction(self.actionSmooth)
        self.toolBars[3].addAction(self.actionSmoothPulses)
        self.actionSmoothPulses.triggered.connect(self.smoothPulses_triggered)
        self.toolBars[3].addAction(self.actionReadPulses)
        self.actionReducePulses = copyAction(self.actionReduceData)
        self.toolBars[3].addAction(self.actionReducePulses)
        self.actionReducePulses.triggered.connect(self.reducePulses_triggered)
        self.toolBars[3].addAction(self.actionReadPulses)
        self.getPulseFromExperiment=QAction(parent=self, text='GetPulse')
        self.toolBars[3].addSeparator()
        self.toolBars[3].addAction(self.getPulseFromExperiment)
        self.getPulseFromExperiment.triggered.connect(self.getPulseFromExperiment_triggered)
        self.repairPulse=QAction(parent=self, text='repairPulse')
        self.toolBars[3].addAction(self.repairPulse)
        self.repairPulse.triggered.connect(self.repairPulse_triggered)
        self.dispersiveShift=QAction(parent=self, text='dispersion')
        self.dispersiveShift.setCheckable(True)
        self.dispersiveShift.setChecked(True)
        self.toolBars[3].addAction(self.dispersiveShift)



#       tab 3 end

        self.toolBars[2].addAction(self.actionSaveExpData)

        self.toolBars[4].addAction(self.actionUpdateDiagramm)
        
        self.corrEAction=QAction(text='Ecor', parent=self, icon=QIcon(":/icons/ui/Ecorr"))
        self.corrEAction.setCheckable(True)
        self.toolBars[5].addAction(self.actionUpdateODBCContent)
        self.toolBars[5].addAction(self.corrEAction)
        self.toolBars[5].addSeparator()
        self.checkAG=QActionGroup(self)
        self.checkAG.addAction(self.actionCheckAll)
        self.checkAG.addAction(self.actionCheckNone)
        self.checkAG.triggered.connect(self.checkAction)
        self.toolBars[5].addAction(self.actionCheckAll)
        self.toolBars[5].addAction(self.actionCheckNone)

        self.toolBars[5].addSeparator()
        self.toolBars[5].addAction(self.actionXLSexport)
        self.toolBars[5].addAction(self.actionCreateReport)
        self.toolBars[5].addSeparator()
        self.actionCalculateMeanCurves=QAction(self, text='Statistic')
        self.toolBars[5].addAction(self.actionCalculateMeanCurves)
        self.actionCalculateMeanCurves.triggered.connect(self.calculateMeanCurves_triggered)
        
        self.actionBetterSyncPulses=QAction(self, text='Sync')
        self.toolBars[5].addAction(self.actionBetterSyncPulses)
        self.actionBetterSyncPulses.triggered.connect(self.betterSyncPulses_triggered)

        self.tabWidget.currentChanged.connect(self.tabChanged)
        self.tbOpenDatabase.setDefaultAction(self.actionOpenDatabase)
        self.cbExpType.currentIndexChanged.connect(self.updateExpNumbers)
        self.cbMaterial.currentIndexChanged.connect(self.updateExpNumbers)

        try:
            self.conf=json.load(open('conf.json','r'))
        except:
            self.conf={}
        odbcName=self.conf.get('odbcFname', '')
        self.odbc=None
        if odbcName and os.path.exists(odbcName):
            self.leDatabaseFile.setText(self.conf['odbcFname'])
            self.odbc=expODBC(self.conf['odbcFname'])
            self.updateODBCcontent()

        self.colors=['r', 'b', 'g']
        self.expData=[]
        self.mplDiagramm.ax2=self.mplDiagramm.ax.twinx()
        self.mplDiagramm.figure.subplots_adjust(right=0.9, top=0.98)
        self.lwExperiments.itemChanged.connect(self.lwExperiments_itemChanged)
        self.mplComparDiag.ax2=self.mplComparDiag.ax.twinx()
        self.mplComparDiag.figure.subplots_adjust(right=0.9, top=0.98)
        if self.mplComparDiag.ax.get_lines():
            self.mplComparDiag.ax.legend()
        self.channels=[]
        self.trDy=self.conf.get('trDy', 1e-4)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()
    
    def dropEvent(self, e):
        for u in e.mimeData().urls():
            print(u.toLocalFile())

    def printToLog(self, text):
        self.lLog.addItem(text)

    def getActiveCurves(self, mpl=None):
        curves=[]
        if not mpl:
            mpl=self.mpls[self.tabWidget.currentIndex()]
        l=mpl.ax.get_lines()
        for i, c in enumerate(self.channels):
            if c.checkState():
                curves.append(l[i])
#        curves=l
        return curves

    @Slot()
    def on_actionOpenDatabase_triggered(self):
        fname=QFileDialog.getOpenFileName(directory='', filter='*.accdb')[0]
        if fname:
            self.leDatabaseFile.setText(fname)
            self.odbc=expODBC(fname)
            self.conf['odbcFname']=fname
            self.updateODBCcontent()

    def updateODBCcontent(self):
        if self.odbc:
            expTypes=self.odbc.getExpTypes()
            self.cbExpType.clear()
            for et in expTypes:
                self.cbExpType.addItem(str(et['ТипЭксперимента'])+' - '+str(et['КодЭксперимента']), et)
            materials=self.odbc.getMaterials()
            self.cbMaterial.clear()
            for m in materials:
                self.cbMaterial.addItem(str(m['Материал'])+' - '+str(m['КодМатериала']), m)
            idxs=self.conf.get('currentExperiment', (0,0,0))
            try:
                self.cbExpType.setCurrentIndex(idxs[1])
                self.cbMaterial.setCurrentIndex(idxs[0])
            except:
                pass
            self.updateExpNumbers()      
            self.lwExperiments.clear()
            self.lwExperiments.setColumnCount(3)
            self.lwExperiments.setHorizontalHeaderLabels(['№', 'de', 'T'])
            self.lwExperiments.setRowCount(self.cbExpNumber.count())
#            print(materials[idxs[0]]['КодМатериала'])
            try:
                self.currentSeries=expTypes[idxs[1]]['КодЭксперимента']+str(materials[idxs[0]]['КодМатериала'])
            except:
                self.currentSeries=expTypes[0]['КодЭксперимента']+str(materials[0]['КодМатериала'])
            for i in range(self.cbExpNumber.count()):
                try:
                    expN = self.cbExpNumber.itemText(i)
                    data = self.odbc.getExperimentData(self.currentSeries+'-'+expN)
#                t=self.cbExpType.itemData(self.cbExpType.currentIndex())['КодЭксперимента']
#                mc=self.cbMaterial.itemData(self.cbMaterial.currentIndex())['КодМатериала']               
#                item=QListWidgetItem(str(t)+str(mc)+'-'+self.cbExpNumber.itemText(i))
                    item=QTableWidgetItem(0)
                    item.setText(expN)
                    #item.setFlags(Qt.ItemIsUserCheckable and Qt.ItemIsEnabled)
                    item.setCheckState(0)
                    self.lwExperiments.setItem(i,0,item)
                    item=QTableWidgetItem(1)
                    try:
                        de = tofloat(data['СкоростьДеформации'])
                    except:
                        de = 0.0
                    item.setText('{:.0f}'.format(de))
                    self.lwExperiments.setItem(i,1,item)
                    item=QTableWidgetItem(2)
                    item.setText('{:.0f}'.format(data['Температура']))
                    self.lwExperiments.setItem(i,2,item)
                except:
                    pass


    def updateExpNumbers(self, idx=0):
        if not self.odbc:
            return
        try:
            t=self.cbExpType.itemData(self.cbExpType.currentIndex())['КодЭксперимента']
            mc=self.cbMaterial.itemData(self.cbMaterial.currentIndex())['КодМатериала']
        except:
            return
        numbers=self.odbc.getNumbers(t, mc)
        self.cbExpNumber.clear()
        nn=[]
        for n in numbers:
            try:
                if n['НомерОбразца']:
                    nn.append(n['НомерОбразца'])
            except:
                pass
        nn.sort()
        for n in nn:
            self.cbExpNumber.addItem('{}'.format(n))
        idxs=self.conf.get('currentExperiment', (0,0,0))
        self.cbExpNumber.setCurrentIndex(idxs[2])

    def tabChanged(self, tb):
        for i in range(self.tabWidget.count()):
            self.toolBars[i].setVisible(False)
        self.toolBars[tb].setVisible(len(self.toolBars[tb].actions()))

    @Slot()
    def on_actionReadData_triggered(self):
        for mpl in self.mpls[:-1]:
            if mpl:
                mpl.ax.clear()
                mpl.ax.grid()
                mpl.nav.interval=None
                mpl.nav.mode=None
        if self.mplOsc.nav.curve.l: self.mplOsc.nav.curve.clear()     
        if not self.odbc:
            return
        try:
            t=self.cbExpType.itemData(self.cbExpType.currentIndex())['КодЭксперимента']
            mc=self.cbMaterial.itemData(self.cbMaterial.currentIndex())['КодМатериала']
            en=self.cbExpNumber.itemText(self.cbExpNumber.currentIndex())
            self.currentExpCode=str(t)+str(mc)+'-'+en
        except:
            return
        self.expData=self.odbc.getExperimentData(self.currentExpCode)
        try:
            self.strickerData=self.odbc.getStrickerData(self.expData['Ударник'])
        except:
            self.strickerData={}
        self.barData=[[],[]]
        try:
            self.barData[0]=self.odbc.getBarData(self.expData['НагружающийСтержень'])
            self.barData[1]=self.odbc.getBarData(self.expData['ОпорныйСтержень'])
        except:
            self.barData=[{},{}]
        if not self.expData['Осциллограмма']:
            self.printToLog('Нет осцилограммы')
            self.mplOsc.ax.clear()
            self.mplOsc.ax.grid()
            self.mplOsc.figure.canvas.draw_idle()

            for c in self.channels:
                self.vlChannels.removeWidget(c)
                c.close()
                del c
            return
        try:
            t, rays=unpackTable(self.expData['Осциллограмма'])
        except:
            t=[]
            rays=[]
        #self.printToLog(str(len(self.channels)))
        for c in self.channels:
            self.vlChannels.removeWidget(c)
            c.close()
            del c
        self.channels=[]
        self.vlChannels.update()
        for i, r in enumerate(rays):
            cb=QCheckBox(str(i+1), self)
            self.channels.append(cb)
            cb.setChecked(True)
            cb.stateChanged.connect(self.cbChannelChecked)
            self.vlChannels.addWidget(cb)
            c, = self.mplOsc.ax.plot(t*1e6, r, label=str(i+1), color=self.colors[i])
#            self.curves.append(c)
        self.mplOsc.figure.canvas.draw_idle()
        self.printToLog('Данные прочитаны')
        self.conf['currentExperiment']=(self.cbMaterial.currentIndex(), self.cbExpType.currentIndex(),
                                        self.cbExpNumber.currentIndex())
        self.tSample.setItem(0,0, QTableWidgetItem(str(self.expData['Длина'])))
        self.tSample.setItem(1,0, QTableWidgetItem(str(self.expData['Диаметр'])))
        self.tSample.setItem(2,0, QTableWidgetItem(str(self.expData['ОстаточнаяДлина'])))
        for i, b in enumerate([self.tBar1, self.tBar2]):
            w=QTableWidgetItem(str(self.barData[i].get('Длина(мм)', 0)))
            w.setFlags(Qt.ItemIsEditable)
            b.setItem(0,0, w)
            w=QTableWidgetItem(str(self.barData[i].get('Диаметр(мм)',0)))
            w.setFlags(Qt.ItemIsEditable)
            b.setItem(4,0, w)
            w=QTableWidgetItem(str(self.barData[i].get('МодульУпругости(МПа)',0)))
            w.setFlags(Qt.ItemIsEditable)
            b.setItem(3,0, w)
            w=QTableWidgetItem(str(self.barData[i].get('СкоростьЗвука(мсек)',0)))
            w.setFlags(Qt.ItemIsEditable)
            b.setItem(2,0, w)
            w=QTableWidgetItem(str(self.barData[i].get('Материал', '')))
            w.setFlags(Qt.ItemIsEditable)
            b.setItem(6,0, w)
        self.tBar1.setItem(1,0, QTableWidgetItem(str(self.expData.get('ПоложениеДатчиковНС(мм)',0))))
        self.tBar2.setItem(1,0, QTableWidgetItem(str(self.expData.get('ПоложениеДатчиковОС(мм)',0))))
        self.tBar1.setItem(5,0, QTableWidgetItem(str(self.expData.get('КалибровочныйКоэффициентНС',0))))
        self.tBar2.setItem(5,0, QTableWidgetItem(str(self.expData.get('КалибровочныйКоэффициентОС',0))))
        self.tStricker.setItem(0,0, QTableWidgetItem(str(self.strickerData.get('ДлинаУдарника(мм)',0))))
        self.tStricker.setItem(1,0, QTableWidgetItem(str(self.strickerData.get('ДиаметрУдарника(мм)',0))))
        self.tStricker.setItem(4,0, QTableWidgetItem(str(self.strickerData.get('МатериалУдарника',0))))
        self.tStricker.setItem(2,0, QTableWidgetItem(str(self.expData.get('СкоростьУдарника',0))))
        self.tStricker.setItem(3,0, QTableWidgetItem(str(self.expData.get('ДавлениеКВД',0))))
        self.tExperiment.setItem(0,0, QTableWidgetItem(str(self.expData.get('КодМатериала',0))))
        self.tExperiment.setItem(1,0, QTableWidgetItem(str(self.expData.get('ТипЭксперимента',0))))
        self.tExperiment.setItem(2,0, QTableWidgetItem(str(self.expData.get('НомерОбразца',0))))
        self.tExperiment.setItem(3,0, QTableWidgetItem(str(self.expData.get('Температура',20))))
        self.tExperiment.setItem(4,0, QTableWidgetItem(str(self.expData.get('Примечание',''))))
        if self.expData['ИмпульсыОбработанные']:
            t, d = unpackTable(self.expData['ИмпульсыОбработанные'])
            if len(d)>=3:
                for dd in d[:3]:
                    if np.mean(dd)<0:
                        dd*=-1.0
                    self.mplPulses.ax.plot(t*1e6, dd)
                self.trDy=(max(d[2])-min(d[2]))/100.
                self.mplPulses.ax.plot(t*1e6, d[0]-d[1], 'k--')
                self.mplPulses.figure.canvas.draw_idle()
        self.updateDiagramm()

    def closeEvent(self, event):
        if self.odbc:
            self.odbc.close()
            json.dump(self.conf, open('conf.json', 'w'))

    def mplRedraw(self, mpl=None):
        if not mpl:
            mpl=self.mpls[self.tabWidget.currentIndex()]
        mpl.ax.set_autoscalex_on(True)
        mpl.ax.set_autoscaley_on(True)
        mpl.ax.relim(True)
        mpl.ax.autoscale_view()
        mpl.figure.canvas.draw_idle()

    def setMode(self, action):
        mpl=action.actionGroup().parent()
        mode=action.data()
        mpl.nav.mode=mode
        if mode in ['interval', 'curve', 'distance']:
            if mpl.tb._active=='ZOOM':
                mpl.tb.zoom()
            if mpl.tb._active=='PAN':
                mpl.tb.pan()
        if mode=='zoom' and mpl.tb._active!='ZOOM':
            mpl.tb.zoom()
        if mode=='pan' and mpl.tb._active!='PAN':
            mpl.tb.pan()
        if mode=="zoom": mpl.setCursor(Qt.CrossCursor)
        if mode=="pan": mpl.setCursor(Qt.OpenHandCursor)
        if mode=="interval": mpl.setCursor(Qt.SizeHorCursor)
        if mode=="curve": mpl.setCursor(Qt.CrossCursor)

    @Slot()
    def on_actionMplHome_triggered(self):
        self.mplRedraw()

    @Slot()
    def on_actionCut_triggered(self):
        ii=self.tabWidget.currentIndex()
        mpl=self.mpls[ii]
        curves=mpl.ax.lines
        if not curves: return
        if not (mpl.nav.interval): return
        x1, x2 = mpl.nav.get_interval()
        dt = x2-x1
        rez, ok = QInputDialog.getDouble(self, "Cut interval", "dt, mks", dt, 0, 100000, 5)
        if not ok: return
        xs = curves[0].get_xdata()
        n1 = np.array(xs).searchsorted(x1)
        n2 = np.array(xs).searchsorted(x1+rez)
        xs=xs[n1:n2]
        xs=(np.array(xs)-xs[0]).tolist()
        for c in curves:
            y=c.get_ydata()[n1:n2]
            c.set_data(xs,y)
        mpl.nav.remove_interval()
        mpl.nav.curve.clear()
        self.mplRedraw()

    @Slot()
    def on_actionZero_triggered(self):
        curves=self.getActiveCurves()       
        if not (self.mplOsc.nav.interval): return
        x1, x2 = self.mplOsc.nav.get_interval()
        for c in curves:
            xs = c.get_xdata()
            ys = c.get_ydata()
            n1 = np.array(xs).searchsorted(x1)
            n2 = np.array(xs).searchsorted(x2)
            if n1==n2: return
            ys-=np.mean(ys[n1:n2])
            c.set_data(xs,ys)
        self.mplRedraw()

    @Slot()
    def on_actionSmooth_triggered(self):
        fltr=self.conf.get('filter', 0)
        fltrs=["FFT filter", "Moving average smoothing"]
        if fltr:
            fltrs.reverse()
        tp, ok = QInputDialog.getItem(self, "Filter type", "Choose a type of filter", fltrs)
        if not ok: return
        curves=self.getActiveCurves()
        if len(curves)==0: return
        if tp=="FFT filter":
            self.conf['filter']=0
            rez, ok = QInputDialog.getInt(self, "Input cut freq", "freq, Hz", self.conf.get('freqCut', 100000), 100, 10000000, 10000)
            if not ok: return
            self.conf['freqCut']=rez
            tmp_curves=[]
            for i, c in enumerate(curves):        
                x = c.get_xdata()
                y = c.get_ydata()
                maxt=max(x)*1e-6
                yy = fft_filter(maxt, y, rez)
                yy = list(yy)+[yy[-1]]*(len(x)-len(yy))
                tmp_curve, = self.mplOsc.ax.plot(x,yy, ["black","brown"][i])
                tmp_curves.append(tmp_curve)
                self.mplRedraw()
        if tp=="Moving average smoothing":
            self.conf['filter']=1
            rez, ok = QInputDialog.getInt(self, "Input window size", "Points", self.conf.get('avePoints', 100), 2, 1000000, 50)
            if not ok: return
            self.conf['avePoints']=rez
            tmp_curves=[]
            for i, c in enumerate(curves):        
                x = c.get_xdata()
                y = c.get_ydata()
                maxt=max(x)*1e-6
                yy = movingAverage(y, rez)
                ##yy = [yy[0]]*(rez//2)+list(yy)+[yy[-1]]*(len(x)-len(yy)-rez//2)
                tmp_curve, = self.mplOsc.ax.plot(x,yy, ["black","brown"][i])
                tmp_curves.append(tmp_curve)
                self.mplRedraw()

        rez = QMessageBox.question(self, "Apply?", "Apply?", QMessageBox.Yes | QMessageBox.No)
        for c,tmp in zip(curves, tmp_curves): 
            if rez == QMessageBox.Yes:
                c.set_data(x,tmp.get_ydata())
            tmp.remove()
        self.mplRedraw() 

    def cbChannelChecked(self, idx):
        mpl=self.mplOsc
        l=mpl.ax.get_lines()
        for i, c in enumerate(self.channels):
            l[i].set_visible(c.checkState())
        self.mplRedraw()

    @Slot()
    def on_actionSaveOSC_triggered(self):
        curves=self.getActiveCurves()
        if not curves: return
        t=np.array(curves[0].get_xdata())*1e-6
        y=[]
        for c in curves:
            y.append(c.get_ydata())
        osc=packTable(t,y)
        self.odbc.putOsc(self.currentExpCode, osc)
        self.expData['Осциллограмма']=osc
#        print(self.currentExpCode)
        self.printToLog('Данные записаны')

    @Slot()
    def on_actionSaveExpData_triggered(self):
        self.expData['Длина']=tofloat(self.tSample.item(0,0).text())
        self.expData['Диаметр']=tofloat(self.tSample.item(1,0).text())
        self.expData['ОстаточнаяДлина']=tofloat(self.tSample.item(2,0).text())
        self.expData['ПоложениеДатчиковНС(мм)']=tofloat(self.tBar1.item(1,0).text())
        self.expData['ПоложениеДатчиковОС(мм)']=tofloat(self.tBar2.item(1,0).text())
        self.expData['КалибровочныйКоэффициентНС']=tofloat(self.tBar1.item(5,0).text())
        self.expData['КалибровочныйКоэффициентОС']=tofloat(self.tBar2.item(5,0).text())
        self.expData['СкоростьУдарника']=tofloat(self.tStricker.item(2,0).text())
        self.expData['Примечание']=str(self.tExperiment.item(4,0).text())
        self.odbc.putInfo(table='Эксперимент',
                          putFields=('Длина', 'Диаметр', 'ОстаточнаяДлина',
                                     'ПоложениеДатчиковНС(мм)', 'ПоложениеДатчиковОС(мм)',
                                     'КалибровочныйКоэффициентНС', 'КалибровочныйКоэффициентОС',
                                     'СкоростьУдарника', 'Примечание'),
                          putFieldsValues=(self.expData['Длина'], self.expData['Диаметр'],
                                           self.expData['ОстаточнаяДлина'],
                                           self.expData['ПоложениеДатчиковНС(мм)'], self.expData['ПоложениеДатчиковОС(мм)'],
                                           self.expData['КалибровочныйКоэффициентНС'], self.expData['КалибровочныйКоэффициентОС'],
                                           self.expData['СкоростьУдарника'],
                                           self.expData['Примечание']),
                          fieldsCond='КодОбразца', fieldsCondValues=self.currentExpCode)
    @Slot()
    def on_actionReadPulses_triggered(self):
        if not self.expData: return
        if not self.expData.get('Осциллограмма', 0): return
#        t,rs=unpackTable(self.expData['Осциллограмма'])
        c=self.getActiveCurves(mpl=self.mplOsc)
        if len(c)!=2:
            self.printToLog('Должно быть выбрано 2 осциллограммы.')
            return
        t=np.array(c[0].get_xdata())
        rs=[c[0].get_ydata(), c[1].get_ydata()]
        sc=1 if self.expData['ТипЭксперимента'] in ['t', 'uv'] else -1
        Ld1=tofloat(self.expData['ПоложениеДатчиковНС(мм)'])
        c1=tofloat(self.barData[0]['СкоростьЗвука(мсек)'])
        d1=tofloat(self.barData[0]['Диаметр(мм)'])
        E1=tofloat(self.barData[0]['МодульУпругости(МПа)'])
        Ld2=tofloat(self.expData['ПоложениеДатчиковОС(мм)'])
        c2=tofloat(self.barData[1]['СкоростьЗвука(мсек)'])
        d2=tofloat(self.barData[1]['Диаметр(мм)'])
        E2=tofloat(self.barData[1]['МодульУпругости(МПа)'])
        self.mplPulses.ax.clear()
        self.mplPulses.ax.grid()
        b1 = barWithDispersion(r0=d1*1e-3/2, E=E1*1e6, rho=E1*1e6/c1**2)
        b2 = barWithDispersion(r0=d2*1e-3/2, E=E2*1e6, rho=E2*1e6/c1**2)
        b1_d = False
        b2_d = False
        if self.barData[0].get('Дисперсия',''):
            b1.load(data=self.barData[0]['Дисперсия'])
            b1_d = self.dispersiveShift.isChecked()
        if self.barData[1].get('Дисперсия',''):
            b2.load(data=self.barData[1]['Дисперсия'])
            b2_d = self.dispersiveShift.isChecked()

        k1=tofloat(self.expData['КалибровочныйКоэффициентНС'])
        k2=tofloat(self.expData['КалибровочныйКоэффициентОС'])
        if b1_d:
            inP = np.array(b1.disp_shift_wave(t*1e-6, rs[0]*sc*k1, Ld1*1e-3))
            refP = np.array(b1.disp_shift_wave(t*1e-6, -rs[0]*sc*k1, -Ld1*1e-3))            
        else:
            inP = np.array(b1.simple_shift_wave(t, rs[0]*sc*k1, Ld1/c1*1000))
            refP = np.array(b1.simple_shift_wave(t, -rs[0]*sc*k1, -Ld1/c1*1000))
        if b2_d:
            trP = np.array(b2.disp_shift_wave(t*1e-6, rs[1]*sc*k2, -Ld2*1e-3))
        else:
            trP = np.array(b2.simple_shift_wave(t, rs[1]*sc*k2, -Ld2/c2*1000))
        tt = t[:len(inP)]
        self.mplPulses.ax.plot(tt, inP)
        self.mplPulses.ax.plot(tt, refP)
        self.mplPulses.ax.plot(tt, trP)
        self.mplPulses.ax.plot(tt, inP-refP, 'k--')
        self.trDy=(max(trP)-min(trP))/100.
        self.mplRedraw()

    @Slot()
    def on_actionSaveToDat_triggered(self):
        if not self.expData: return
        if not self.barData: return
        f,ok = QFileDialog.getSaveFileName(directory=self.conf.get('lastDatDir','.')
                                           +os.sep+self.currentExpCode, filter='*.dat')
        if ok:
            saveDAT(f, self.expData, self.barData)
            self.conf['lastDatDir']=os.path.dirname(os.path.abspath(f))

    @Slot()
    def on_actionSavePulses_triggered(self):
        l=self.mplPulses.ax.get_lines()
        if len(l)<4: return
        t=np.array(l[0].get_xdata())*1e-6
        ys=[]
        for ll in l[:-1]:
            ys.append(ll.get_ydata())
        p=packTable(t, ys)
        self.expData['ИмпульсыОбработанные'] = p
        self.odbc.putPulses(self.currentExpCode, p)

    def updateDiagramm(self):
        l=self.mplPulses.ax.get_lines()
        if len(l)<4: return
        self.mplDiagramm.ax.clear()
        self.mplDiagramm.ax2.clear()
        t, et, st, det=self.calculateDiagram(self.currentExpCode)
        dde=meanDE({'et': et, 'st': st, 'de': det})
        self.mplDiagramm.ax.plot(et,st)
        self.mplDiagramm.ax2.plot(et,det,'r--')
#        print(dde)
        self.mplDiagramm.ax2.axhline(dde, color='k', ls='--')   
        self.mplDiagramm.ax2.text(0,dde*1.01, '{:.1f}'.format(dde))
        self.mplDiagramm.ax.grid()
        self.mplDiagramm.figure.canvas.draw_idle()

    def calculateDiagram(self, expCode, pulses=None):
        expData=self.odbc.getExperimentData(expCode)
        if not pulses:
            if not expData['ИмпульсыОбработанные']: return
            t, ys=unpackTable(expData['ИмпульсыОбработанные'])
        else:
            t, ys = pulses
        ys=np.array(ys)
        for i in range(len(ys)):
            if np.mean(ys[i])<0:
                ys[i]*=-1.0
        b1=self.odbc.getBarData(expData['НагружающийСтержень'])
        b2=self.odbc.getBarData(expData['ОпорныйСтержень'])
        cfg={}
        cfg['c1']=tofloat(b1['СкоростьЗвука(мсек)'])
        cfg['c2']=tofloat(b2['СкоростьЗвука(мсек)'])
        cfg['E2']=tofloat(b2['МодульУпругости(МПа)'])
        D=tofloat(b2['Диаметр(мм)'])
        D0=tofloat(b2['ВнутреннийДиаметр'])
        cfg['S2']=np.pi*(D**2-D0**2)/4.
        cfg['Ssp']=np.pi*tofloat(expData['Диаметр'])**2/4.
        cfg['Lsp']=tofloat(expData['Длина'])*1e-3
        et,st,det=calcDiagram(t[1]-t[0], [ys[0]], [ys[1]], [ys[2]], cfg,
                              isCorrE=self.corrEAction.isChecked(),
                              Ecor=self.conf.get('Ecor', 100000.))
        return np.array(t)*1e6, et, st, det

    @Slot()
    def on_actionUpdateDiagramm_triggered(self):
        self.updateDiagramm()

    @Slot()
    def on_actionOpenOSC_triggered(self):
        if self.mplOsc.nav.curve.l: self.mplOsc.nav.curve.clear()           
        fname=QFileDialog.getOpenFileName(self,"Select File",self.conf.get('lastdir',''),"all(*.lvm *.lvz *.npz *.tsv *.dat *.csv *.tdms *.osc);;\
    labview files (*.lvm *.lvz *.tdms);; npz-files (*.npz);; txt-files (*.txt);; agilent data (*.tsv);; dat-file (*.dat);; Microsoft csv (*.csv);; Ocsiloscope data (*.osc)")
        if fname=="": return
        fname=str(fname[0])
#        self.action
        self.conf['lastdir'] = os.path.dirname(fname)
        if self.mplOsc.nav.interval: self.mplOsc.nav.remove_interval()
        if fname[-3:].upper()=='LVM' or fname[-3:].upper()=='LVZ' :
            x,y1,y2 = lvmopen(fname)
        elif fname[-3:].upper()=='NPZ':
            x,y1,y2=load_npz(fname)
        elif fname[-3:].upper()=='TXT':
            data=np.loadtxt(fname, unpack=True,skiprows=2)
            x=data[0]
            y1=data[1]
            y2=data[2]
            rays = [y1, y2]
        elif fname[-3:].upper()=='TSV':
            data=np.loadtxt(fname, unpack=True)
            x=data[0]
            y1=data[3]
            y2=data[4]
        elif fname[-3:].upper()=='DAT':
            d=dat_file(fname)
            byte_rays=d.byte_rays
            y1=np.array(byte_rays[0])*d.diapA
            y2=np.array(byte_rays[1])*d.diapB
            x=np.array(list(range(1024)))*d.dt*1e-6
        elif fname[-3:].upper()=='CSV':
            data=np.loadtxt(fname, unpack=True,skiprows=1, delimiter=',',usecols=(0,1,2))
            x=data[0]
            y1=data[1]
            y2=data[2]
#        elif fname[-4:].upper()=='TDMS':
#            objects, rawdata=pytdms.read(fname)
#            x=rawdata["/'Untitled'/'Time'"]
#            y1=rawdata["/'Untitled'/'Untitled 1'"]
#            y2=rawdata["/'Untitled'/'Untitled 2'"]
        elif fname[-3:].upper()=='OSC':
            channels=np.load(fname)['data']
            self.cCount=len(channels)
            if len(channels)<2:
                return
            idx1=0
            idx2=1
            dt=channels[0]["dt"]
            n=len(channels[0]["data"])
            x=np.linspace(0,dt*n,n)
            # if len(channels)>2:
            #     dlg=raySelectionDlg(self)
            #     if not dlg.exec_():
            #         return
            #     idx1=dlg.cbRay1.currentIndex()
            #     idx2=dlg.cbRay2.currentIndex()
            # self.conf['oscRay1']=idx1
            # self.conf['oscRay2']=idx2
            rays = []
            for c in channels:
                rays.append(c['y0']+c['dy']*c['data'])
            # y1=channels[idx1]['y0']+channels[idx1]['dy']*channels[idx1]['data']
            # y2=channels[idx2]['y0']+channels[idx2]['dy']*channels[idx2]['data']
        else:
            return
        x = np.array(x)*1e6
        x-=x[0]
        self.mplOsc.ax.clear()
        self.mplOsc.ax.grid()

        for c in self.channels:
            self.vlChannels.removeWidget(c)
            c.close()
            del c

        self.channels=[]
        self.vlChannels.update()
        for i, r in enumerate(rays):
            cb=QCheckBox(str(i+1), self)
            self.channels.append(cb)
            cb.setChecked(True)
            cb.stateChanged.connect(self.cbChannelChecked)
            self.vlChannels.addWidget(cb)
            self.mplOsc.ax.plot(x,r)

        self.mplOsc.nav.curve.clear()
#        self.mpl.ax.relim()
#        self.mpl.ax.autoscale()
        self.mplOsc.figure.canvas.draw_idle()

    @Slot()
    def on_actionUpdateODBCContent_triggered(self):
        checked=[]
        for i in range(self.lwExperiments.rowCount()):
            ii=self.lwExperiments.item(i,0)
            if ii.checkState():        
                checked.append(ii.text())
        self.updateODBCcontent()
        self.mplComparDiag.ax.clear()
        self.mplComparDiag.ax2.clear()
        self.mplComparDiag.ax.grid()
        if self.mplComparDiag.ax.get_lines():
            self.mplComparDiag.ax.legend()
        self.mplComparDiag.figure.canvas.draw_idle()
        for i in range(self.lwExperiments.rowCount()):
            ii=self.lwExperiments.item(i,0)
            if ii.text() in checked:
                ii.setCheckState(2)

    def lwExperiments_itemChanged(self, item):
        if item.column()!=0:
            return
        if not item.data(100) and item.checkState()==2:
            t=self.cbExpType.itemData(self.cbExpType.currentIndex())['КодЭксперимента']
            mc=self.cbMaterial.itemData(self.cbMaterial.currentIndex())['КодМатериала']               
            expCode=str(t)+str(mc)+'-'+item.text()
            try:
                idxs=[0,0,0]
                for i, rbg in enumerate(self.radioButtons):
                    for j, rb in enumerate(rbg):
                        if rb.isChecked():
                            idxs[i] = j
                data=self.calculateDiagram(expCode)
                l1,=self.mplComparDiag.ax.plot(data[idxs[0]], data[idxs[1]], label=expCode)
                l2=None
                if idxs[2]<4:
                    l2,=self.mplComparDiag.ax2.plot(data[idxs[0]], data[idxs[2]], '--', lw=1, color=l1.get_color())
                item.setData(100, (l1,l2))
                item.setData(101, expCode)
                self.idxs = idxs
            except:
                pass
        if item.data(100) and item.checkState()==0:
            for l in item.data(100):
                l.remove()
            item.setData(100, None)
            item.setData(101, None)
        self.mplComparDiag.ax.relim()
        if self.mplComparDiag.ax.get_lines():
            self.mplComparDiag.ax.legend()
        self.mplComparDiag.figure.canvas.draw_idle()

    @Slot()
    def on_actionSyncPulses_triggered(self):
        l=self.mplPulses.ax.get_lines()
        p=[l[0].get_xdata(), [l[0].get_ydata(), l[1].get_ydata(), l[2].get_ydata()]]
        pp=syncPulses(p)
        l[0].set_ydata(pp[1][0])
        l[1].set_ydata(pp[1][1])
        l[2].set_ydata(pp[1][2])
        l[3].set_ydata(pp[1][0]-pp[1][1])
        self.mplRedraw()

    @Slot()
    def on_actionReduceData_triggered(self):
        l=self.mplOsc.ax.get_lines()
        if len(l)<1: return
        xs = np.array(l[0].get_xdata())
        rez, ok = QInputDialog.getInt(self, "Thinout degree", "Current number of points is %d. Devide by" % (len(xs),), 10, 1, 1000000, 10)
        if not ok: return
        if rez>=len(xs): return
        for ll in l:
            y = ll.get_ydata()
            ll.set_xdata(xs[::rez])
            ll.set_ydata(y[::rez])
        self.mplOsc.figure.canvas.draw_idle()
    
    @Slot()
    def on_actionApplyCurve_triggered(self):
        if not self.mplOsc.nav.curve.l: return
        curves=self.getActiveCurves()
        if len(curves)==0: return
        for c in curves:
            xs, ys = list(zip(*np.sort(np.array(self.mplOsc.nav.curve.points,dtype=[("x",float),("y",float)]),order="x")))    
            n1=np.searchsorted(c.get_xdata(),xs[0])
            n2=np.searchsorted(c.get_xdata(),xs[-1])
            xx=c.get_xdata()[n1:n2]
            yy=np.interp(xx,xs,ys)
            zz=c.get_ydata()
            zz[n1:n2]=yy
            c.set_ydata(zz)
        self.mplOsc.nav.curve.clear()
        self.mplOsc.figure.canvas.draw_idle() 
    
    @Slot()
    def on_actionDeleteLine_triggered(self):
        if self.mplOsc.nav.curve.l: self.mplOsc.nav.curve.clear() 
        
    @Slot()
    def on_actionCompressCurve_triggered(self):
        curves=self.getActiveCurves()
        if self.mplOsc.nav.interval:
            x1, x2 = self.mplOsc.nav.get_interval()
        elif self.mplOsc.nav.curve.l:
                xx=self.mplOsc.nav.curve.l.get_xdata()
                x1=min(xx)
                x2=max(xx)
        else:
            return
        for c in curves:
            xs = c.get_xdata()
            ys = c.get_ydata()
            n1 = np.array(xs).searchsorted(x1)
            n2 = np.array(xs).searchsorted(x2)
            if n1==n2: return
            x1=xs[n1]
            x2=xs[n2]
            y1=ys[n1]
            y2=ys[n2]
            if self.mplOsc.nav.curve.l:
                xxs, yys = list(zip(*np.sort(np.array(self.mplOsc.nav.curve.points,dtype=[("x",float),("y",float)]),order="x")))    
                f=lambda x: np.interp(x,xxs,yys)                
            else:
                f=lambda x: (x-x1)/(x2-x1)*(y2-y1)+y1
            smax=np.abs(ys[n1:n2]-f(np.array(xs[n1:n2]))).max()
            pwr=20
#            if self.actionExp.isChecked():
#            g=lambda s: 1./np.exp(np.log(2.)*(s/smax)**pwr)
#            else:
            g=lambda s: 0.5
            for n in range(n1+1,n2):
                ss=ys[n]-f(xs[n])
                ys[n]=g(np.abs(ss))*ss+f(xs[n])
            c.set_data(xs,ys)
        self.mplOsc.figure.canvas.draw_idle()

    @Slot()
    def on_actionPolyFit_triggered(self):
        m, ok=QInputDialog.getInt(self,'Порядок полинома','m', value=5, min=1, max=100)
        c=self.getActiveCurves()
        if type(c)==list:
            c=c[0]
        if (not ok) or (not self.mplOsc.nav.interval) or (not c): return
        x1, x2 = self.mplOsc.nav.get_interval()
        xs = c.get_xdata()
        ys = c.get_ydata()
        n1 = np.array(xs).searchsorted(x1)
        n2 = np.array(xs).searchsorted(x2)
        if n1==n2: return
        xs=xs[n1:n2]
        ys=ys[n1:n2]
        p=np.polyfit(xs,ys,m)
        ys=np.polyval(p,xs)
        self.mplOsc.nav.curve.points=list(zip(xs,ys))
        self.mplOsc.figure.canvas.draw_idle()
    
    def checkAction(self, act):
        toDo=act==self.actionCheckAll
        for i in range(self.lwExperiments.rowCount()):
            self.lwExperiments.item(i,0).setCheckState(2 if toDo else 0)
        
    @Slot()
    def on_actionXLSexport_triggered(self):
        f=QFileDialog.getSaveFileName(filter='*.xls')
        if not f:
            return
        xls=xlwt.Workbook()
        expPars=xls.add_sheet('параметры испытаний')
        t=self.cbExpType.itemData(self.cbExpType.currentIndex())['КодЭксперимента']
        mc=self.cbMaterial.itemData(self.cbMaterial.currentIndex())['КодМатериала']        
        header=['Код испытания', 'Длина ударника(мм)', 'Материал ударника', 'Скорость ударника(м/c)',
                'Температура', 'Скорость деформации', 'Длина(мм)', 'Диаметр(мм)', 'Остаточная длина(мм)',
                'Пластическая деформация(%)', 'Примечание', 'Дата испытания']
        if t=='t':
            header.insert(-3, 'Диаметр шейки(мм)')
            header.insert(-3, 'Предельное удлинение(%)')
            header.insert(-3, 'Предельное сужение(%)')
        for i, h in enumerate(header):
            expPars.write(0,i,h)
        row=1
        N=self.lwExperiments.rowCount()
        progress=QProgressDialog()
        progress.setWindowModality(Qt.WindowModal)
        progress.setMaximum(N)
        progress.setMinimum(0)
        progress.show()
    
        progress.setValue(0)        
        for i in range(N):
            QCoreApplication.processEvents()
            if progress.wasCanceled():
                break            
            ii=self.lwExperiments.item(i,0)
            if ii.checkState():
                expCode=str(t)+str(mc)+'-'+ii.text()
                rep=self.prepareRepData(expCode)
                expPars.write(row,0,rep['expCode'])
                expPars.write(row,1,rep['strikerL'])
                expPars.write(row,2,rep['strikerMat'])
                expPars.write(row,3,rep['strikerV'])
                expPars.write(row,4,rep['expTemp'])
                expPars.write(row,5,rep['expDE'])
                expPars.write(row,6,rep['sampleL'])
                expPars.write(row,7,rep['sampleD'])
                expPars.write(row,8,rep['sampleLL'])
                if t=='t':
                    expPars.write(row,9,rep['sampleDD'])
                    expPars.write(row,10,rep['delta'])
                    expPars.write(row,11,rep['ksi'])
                expPars.write(row,header.index('Пластическая деформация(%)'), rep.get('ep',0))
                expPars.write(row,header.index('Примечание'), rep['expRemark'])
                expPars.write(row,header.index('Дата испытания'), rep['expDate'])
                sh=xls.add_sheet(expCode)
                h2=['время(мкс)', 'падающий', 'отраженный', 'прошедший', 'падающий-отраженный',
                    'деформация', 'напряжение(МПа)', 'скорость деформации(1/c)', 'деф(лог)',
                    'напр(ист)МПа', "скор.деф.(ист)1/c"]
                for j, h in enumerate(h2):
                    sh.write(0,j,h)
                p=rep['pulses']
                if rep['diag']:
                    d=rep['diag'][1:]
                    diag = {'et': d[0], 'st': d[1], 'det': d[2]}
                    toReal(diag, t)
                row+=1
                progress.setValue(i)
                N=len(p[0])
                NN = 1 if N<=500 else N//500
                if not p or not d:
                    continue
                j=0
                for k in range(0, N , NN):
                    sh.write(1+j,0, p[0][k]*1e6)
                    sh.write(1+j,1, p[1][0][k])
                    sh.write(1+j,2, p[1][1][k])
                    sh.write(1+j,3, p[1][2][k])
                    sh.write(1+j,4, p[1][0][k]-p[1][1][k])
                    sh.write(1+j,5, d[0][k])
                    sh.write(1+j,6, d[1][k])
                    sh.write(1+j,7, d[2][k])
                    sh.write(1+j,8, diag['er'][k])            
                    sh.write(1+j,9, diag['sr'][k])            
                    sh.write(1+j,10, diag['der'][k]) 
                    j+=1           
        xls.save(f[0])
        progress.close()

    @Slot()
    def on_actionCreateReport_triggered(self):
        dr = QFileDialog.getExistingDirectory()
        if not dr:
            return
        t=self.cbExpType.itemData(self.cbExpType.currentIndex())['КодЭксперимента']
        mc=self.cbMaterial.itemData(self.cbMaterial.currentIndex())['КодМатериала'] 
        N=self.lwExperiments.rowCount()
        progress=QProgressDialog()
        progress.setWindowModality(Qt.WindowModal)
        progress.setMaximum(N)
        progress.setMinimum(0)
        progress.show()
        
        progress.setValue(0)
        for i in range(N):
            QCoreApplication.processEvents()
            if progress.wasCanceled():
                break
            ii=self.lwExperiments.item(i,0)
            if ii.checkState():
                expCode=str(t)+str(mc)+'-'+ii.text()
                rep=self.prepareRepData(expCode)
                createReport(rep, dr)
            progress.setValue(i)
#            progress.update()
        progress.close()
        
    def prepareRepData(self, expCode):
        rep={}
        rep['expCode']=expCode
        expData=self.odbc.getExperimentData(expCode)
        b1=self.odbc.getBarData(expData['НагружающийСтержень'])
        b2=self.odbc.getBarData(expData['ОпорныйСтержень'])
        st=self.odbc.getStrickerData(expData['Ударник'])
        m=self.odbc.getInfo('МатериалЭксперимент','КодМатериала', expData['КодМатериала'])[0]
        etype=self.odbc.getInfo('ТипЭксперимента', 'КодЭксперимента', expData['ТипЭксперимента'])[0]
        try:
            rep['diag']=self.calculateDiagram(expCode)
        except:
            rep['diag']=[[],[],[],[]]
        t, ys=unpackTable(expData['ИмпульсыОбработанные'])
        ys=np.array(ys)
        for i in range(len(ys)):
            if np.mean(ys[i])<0:
                ys[i]*=-1.0
        rep['pulses']=[t, ys]
        rep['expDate']=''#str(expData['Дата']).split()[0]
        rep['expTime']=''
        rep['expTemp']=tofloat(expData['Температура'])
        rep['expRemark']=str(expData['Примечание'])
        if rep['expRemark']=='None':
            rep['expRemark']=''
        rep['strikerV']=tofloat(expData['СкоростьУдарника'])
        rep['sampleL']=tofloat(expData['Длина'])
        rep["strikerL"]=tofloat(st['ДлинаУдарника(мм)'])
        rep["strikerMat"]=str(st['МатериалУдарника'])
        rep['sampleD']=tofloat(expData['Диаметр'])
        rep['sampleS']=np.pi*tofloat(expData['Диаметр'])**2/4.0
        try:
            print(expCode)
            rep['expDE']=meanDE(dict(zip(['et', 'st', 'de'], rep['diag'][1:])))
        except:
            print('Cant calculate meanDE')
            rep['expDE']=tofloat(expData['СкоростьДеформации'])
        rep['sampleLL']=LL=tofloat(expData['ОстаточнаяДлина'])
        if rep['expCode'][0]=='c':
            rep['ep']=abs(np.log(LL/rep['sampleL']))*100 if LL and rep['sampleL'] else 0
        elif rep['expCode'][0]=='t':
            rep['sampleDD']=DD=tofloat(expData['Шейка'])
            D=tofloat(expData['Диаметр'])
            L=tofloat(expData['Длина'])
            rep['delta']=(LL-L)/L*100
            if rep['delta']<0:
                rep['delta']=0
            rep['ksi']=(D**2-DD**2)/D**2*100 if D else 0
            rep['ep']=2*np.log(D/DD)*100 if DD else 0
        
        rep['matName']=m['Материал']
        rep['matCondition']=''
        rep['expType']=etype['ТипЭксперимента']
        rep["expSetup"]="РСГ-{}".format(b1['Диаметр(мм)'])
        rep["expChief"]=expData['ОтветственныйЗаИспытания']
        rep["roomTemp"]=expData['ТемператураПомещения']
        rep["roomWetness"]=expData['Влажность']
        rep["sampleRemark"]=""
        rep["bar1Mat"]=b1['Материал']
        rep["bar2Mat"]=b2['Материал']
        rep["bar1S"]=tofloat(b1['Диаметр(мм)'])**2*3.14/4.
        rep["bar2S"]=tofloat(b2['Диаметр(мм)'])**2*3.14/4.
        rep["bar1E"]=b1['МодульУпругости(МПа)']
        rep["bar2E"]=b2['МодульУпругости(МПа)']
        rep["bar1C"]=tofloat(b1['СкоростьЗвука(мсек)'])
        rep["bar2C"]=tofloat(b2['СкоростьЗвука(мсек)'])
        rep["bar1K"]=expData['КалибровочныйКоэффициентНС']
        rep["bar2K"]=expData['КалибровочныйКоэффициентОС']
        rep["bar1L"]=b1['Длина(мм)']
        rep["bar2L"]=b2['Длина(мм)']
        rep["gauge1Position"]=expData['ПоложениеДатчиковНС(мм)']
        rep["gauge2Position"]=expData['ПоложениеДатчиковОС(мм)']
        rep["barsRemark"]=""
        rep["strikerD"]=st['ДиаметрУдарника(мм)']
        rep["logoImg"]="logo2.jpg"
        rep["syncImg"]=""
        rep["diagrImg"]=""
        rep["tableLines"]=''
        rep["expAdditionalCells"]=""        
        return rep
    
    def getRayFromExperiment_triggered(self):
        l=[]
        for i in range(self.cbExpNumber.count()):
            l.append(self.cbExpNumber.itemText(i))
        idx, ok=QInputDialog.getItem(self, "Choose experiment index",
                                 "experiment index", l, editable=False)
        if ok:
            r=self.odbc.getExperimentData(self.currentExpCode.split('-')[0]+'-'+idx)['Осциллограмма']
            t,rr=unpackTable(r)
            l=self.mplOsc.ax.get_lines()
            newYY=np.interp(l[0].get_xdata(), np.array(t)*1e6, rr[0])
            l[0].set_ydata(newYY)
            self.mplRedraw()
            
    def getPulseFromExperiment_triggered(self):
        l=[]
        for i in range(self.cbExpNumber.count()):
            l.append(self.cbExpNumber.itemText(i))
        idx, ok=QInputDialog.getItem(self, "Choose experiment index",
                                 "experiment index", l, editable=False)
        if ok:
            r=self.odbc.getExperimentData(self.currentExpCode.split('-')[0]+'-'+idx)['ИмпульсыОбработанные']
            t,rr=unpackTable(r)
            idx2, ok=QInputDialog.getItem(self, "Choose pulse index",
                                          "pulse index", ['1', '2', '3'],
                                          editable=False)
            if ok:
                l=self.mplPulses.ax.get_lines()
                i=int(idx2)-1
                newYY=np.interp(l[i].get_xdata(), np.array(t)*1e6, rr[i])
                l[i].set_ydata(newYY)
                self.mplRedraw()

    def repairPulse_triggered(self):
        idx, ok=QInputDialog.getItem(self, "Choose pulse to repair",
                                      "pulse index", ['1', '2', '3'],
                                      editable=False)
        if ok:
            p=int(idx)-1
            l=self.mplPulses.ax.get_lines()
            if p==2:
                l[2].set_ydata(l[0].get_ydata()-l[1].get_ydata())
            if p==0:
                l[0].set_ydata(l[1].get_ydata()+l[1].get_ydata())
                l[3].set_ydata(l[0].get_ydata()-l[1].get_ydata())
            if p==1:
                l[1].set_ydata(l[0].get_ydata()-l[2].get_ydata())
                l[3].set_ydata(l[0].get_ydata()-l[1].get_ydata())
            self.mplRedraw()

    def calculateMeanCurves_triggered(self):
        return
        N = self.lwExperiments.count()
        for i in range(N):
            ii = self.lwExperiments.item(i,0)
            if ii.checkState():
                pass

    def betterSyncPulses_triggered(self):
        selectedItems = self.lwExperiments.selectedItems()
        if not selectedItems:
            return
        item_to_sync = selectedItems[0]
        if item_to_sync.checkState()!=2:
            return
        self.lines=item_to_sync.data(100)
        self.exp_code_to_sync = item_to_sync.data(101)
        sync_dialog = MySyncDialog(self)
        rez = sync_dialog.exec_()
        if rez:
            p=packTable(sync_dialog.sync_pulses[0], sync_dialog.sync_pulses[1])
            self.odbc.putPulses(self.exp_code_to_sync, p)
            l=self.mplPulses.ax.get_lines()
            l[0].set_data(sync_dialog.sync_pulses[0]*1e6, sync_dialog.sync_pulses[1][0])
            l[1].set_data(sync_dialog.sync_pulses[0]*1e6, sync_dialog.sync_pulses[1][1])
            l[2].set_data(sync_dialog.sync_pulses[0]*1e6, sync_dialog.sync_pulses[1][2])
            l[3].set_data(sync_dialog.sync_pulses[0]*1e6, sync_dialog.sync_pulses[1][0]-sync_dialog.sync_pulses[1][1])
            self.mplRedraw(self.mplPulses)
        self.on_actionUpdateODBCContent_triggered()     
    
    def smoothPulses_triggered(self):
        fltr=self.conf.get('filter', 0)
        fltrs=["FFT filter", "Moving average smoothing"]
        if fltr:
            fltrs.reverse()
        tp, ok = QInputDialog.getItem(self, "Filter type", "Choose a type of filter", fltrs)
        if not ok: return
        allcurves=self.mplPulses.ax.get_lines()
        curves=allcurves[0:3]
        if len(curves)==0: return
        if tp=="FFT filter":
            self.conf['filter']=0
            rez, ok = QInputDialog.getInt(self, "Input cut freq", "freq, Hz", self.conf.get('freqCut', 100000), 100, 10000000, 10000)
            if not ok: return
            self.conf['freqCut']=rez
            tmp_curves=[]
            for i, c in enumerate(curves):        
                x = c.get_xdata()
                y = c.get_ydata()
                maxt=max(x)*1e-6
                yy = fft_filter(maxt, y, rez)
                yy = list(yy)+[yy[-1]]*(len(x)-len(yy))
                tmp_curve, = self.mplPulses.ax.plot(x,yy, "brown")
                tmp_curves.append(tmp_curve)
        if tp=="Moving average smoothing":
            self.conf['filter']=1
            rez, ok = QInputDialog.getInt(self, "Input window size", "Points", self.conf.get('avePoints', 100), 2, 1000000, 50)
            if not ok: return
            self.conf['avePoints']=rez
            tmp_curves=[]
            for i, c in enumerate(curves):        
                x = c.get_xdata()
                y = c.get_ydata()
                maxt=max(x)*1e-6
                yy = movingAverage(y, rez)
                #yy = [yy[0]]*(rez//2)+list(yy)+[yy[-1]]*(len(x)-len(yy)-rez//2)
                tmp_curve, = self.mplPulses.ax.plot(x,yy, "brown")
                tmp_curves.append(tmp_curve)
        self.mplRedraw()

        rez = QMessageBox.question(self, "Apply?", "Apply?", QMessageBox.Yes | QMessageBox.No)
        for c,tmp in zip(curves, tmp_curves): 
            if rez == QMessageBox.Yes:
                c.set_data(x,tmp.get_ydata())
            tmp.remove()
        if rez == QMessageBox.Yes:
           allcurves[3].set_data(x, curves[0].get_ydata()-curves[1].get_ydata())
        self.mplRedraw() 

    def reducePulses_triggered(self):
        l=self.mplPulses.ax.get_lines()
        if len(l)<1: return
        xs = np.array(l[0].get_xdata())
        rez, ok = QInputDialog.getInt(self, "Thinout degree", "Current number of points is %d. Devide by" % (len(xs),), 10, 1, 1000000, 10)
        if not ok: return
        if rez>=len(xs): return
        for ll in l:
            y = ll.get_ydata()
            ll.set_xdata(xs[::rez])
            ll.set_ydata(y[::rez])
        self.mplPulses.figure.canvas.draw_idle()     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())