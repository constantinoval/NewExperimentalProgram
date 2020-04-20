# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lvm_proc.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(676, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Gnome-Applications-Accessories-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mplwidget = MatplotlibWidget(self.centralwidget)
        self.mplwidget.setObjectName("mplwidget")
        self.verticalLayout.addWidget(self.mplwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 676, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/fileopen-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/filesave-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionBoxZoom = QtWidgets.QAction(MainWindow)
        self.actionBoxZoom.setCheckable(True)
        self.actionBoxZoom.setChecked(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Gnome-Zoom-Fit-Best-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBoxZoom.setIcon(icon3)
        self.actionBoxZoom.setObjectName("actionBoxZoom")
        self.actionPan = QtWidgets.QAction(MainWindow)
        self.actionPan.setCheckable(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Mouse_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon4)
        self.actionPan.setObjectName("actionPan")
        self.actionInterval = QtWidgets.QAction(MainWindow)
        self.actionInterval.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Pen-marker-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionInterval.setIcon(icon5)
        self.actionInterval.setObjectName("actionInterval")
        self.actionCut = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Gnome-Edit-Cut-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon6)
        self.actionCut.setObjectName("actionCut")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/Error-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon7)
        self.actionExit.setObjectName("actionExit")
        self.actionShowPos = QtWidgets.QAction(MainWindow)
        self.actionShowPos.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/altimeter_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShowPos.setIcon(icon8)
        self.actionShowPos.setObjectName("actionShowPos")
        self.actionDrawCurve = QtWidgets.QAction(MainWindow)
        self.actionDrawCurve.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDrawCurve.setIcon(icon9)
        self.actionDrawCurve.setObjectName("actionDrawCurve")
        self.actionApplyCurve = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/apply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionApplyCurve.setIcon(icon10)
        self.actionApplyCurve.setObjectName("actionApplyCurve")
        self.actionClearCurve = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/trash-full.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClearCurve.setIcon(icon11)
        self.actionClearCurve.setObjectName("actionClearCurve")
        self.actionDistance = QtWidgets.QAction(MainWindow)
        self.actionDistance.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/measure.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDistance.setIcon(icon12)
        self.actionDistance.setObjectName("actionDistance")
        self.actionLowPassFilter = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/filter_32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLowPassFilter.setIcon(icon13)
        self.actionLowPassFilter.setObjectName("actionLowPassFilter")
        self.actionScaleY = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/Fullscreen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScaleY.setIcon(icon14)
        self.actionScaleY.setObjectName("actionScaleY")
        self.actionRayA = QtWidgets.QAction(MainWindow)
        self.actionRayA.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/Blue Ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRayA.setIcon(icon15)
        self.actionRayA.setObjectName("actionRayA")
        self.actionRayB = QtWidgets.QAction(MainWindow)
        self.actionRayB.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/Green Ball.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRayB.setIcon(icon16)
        self.actionRayB.setObjectName("actionRayB")
        self.actionExp = QtWidgets.QAction(MainWindow)
        self.actionExp.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon17.addPixmap(QtGui.QPixmap(":/icons/exp.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExp.setIcon(icon17)
        self.actionExp.setObjectName("actionExp")
        self.actionPolyfit = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/polyfit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPolyfit.setIcon(icon18)
        self.actionPolyfit.setObjectName("actionPolyfit")
        self.actionThinout = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/icons/thinout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionThinout.setIcon(icon19)
        self.actionThinout.setObjectName("actionThinout")
        self.actionSave_copy_from_setup = QtWidgets.QAction(MainWindow)
        self.actionSave_copy_from_setup.setIcon(icon2)
        self.actionSave_copy_from_setup.setObjectName("actionSave_copy_from_setup")
        self.actionZero = QtWidgets.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/icons/zero.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionZero.setIcon(icon20)
        self.actionZero.setObjectName("actionZero")
        self.actionScaleRays = QtWidgets.QAction(MainWindow)
        self.actionScaleRays.setObjectName("actionScaleRays")
        self.actionExchangeRays = QtWidgets.QAction(MainWindow)
        self.actionExchangeRays.setObjectName("actionExchangeRays")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSave)
        self.menu_File.addAction(self.actionSave_copy_from_setup)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionBoxZoom)
        self.menuEdit.addAction(self.actionPan)
        self.menuEdit.addAction(self.actionInterval)
        self.menuEdit.addAction(self.actionShowPos)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menu.addAction(self.actionRayA)
        self.menu.addAction(self.actionRayB)
        self.menu.addSeparator()
        self.menu.addAction(self.actionScaleRays)
        self.menu.addAction(self.actionExchangeRays)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBoxZoom)
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionInterval)
        self.toolBar.addAction(self.actionDistance)
        self.toolBar.addAction(self.actionShowPos)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionLowPassFilter)
        self.toolBar.addAction(self.actionThinout)
        self.toolBar.addAction(self.actionZero)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDrawCurve)
        self.toolBar.addAction(self.actionPolyfit)
        self.toolBar.addAction(self.actionApplyCurve)
        self.toolBar.addAction(self.actionClearCurve)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionScaleY)
        self.toolBar.addAction(self.actionExp)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRayA)
        self.toolBar.addAction(self.actionRayB)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lvm edit"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu.setTitle(_translate("MainWindow", "Обрабатывать лучи"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionOpen.setToolTip(_translate("MainWindow", "Открыть файл"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionSave.setToolTip(_translate("MainWindow", "Сохранить файл"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionBoxZoom.setText(_translate("MainWindow", "BoxZoom"))
        self.actionBoxZoom.setToolTip(_translate("MainWindow", "Масштабирование изображения"))
        self.actionBoxZoom.setShortcut(_translate("MainWindow", "Z"))
        self.actionPan.setText(_translate("MainWindow", "Pan"))
        self.actionPan.setToolTip(_translate("MainWindow", "Перетаскивание"))
        self.actionPan.setShortcut(_translate("MainWindow", "P"))
        self.actionInterval.setText(_translate("MainWindow", "Interval"))
        self.actionInterval.setToolTip(_translate("MainWindow", "Выделение интервала"))
        self.actionInterval.setShortcut(_translate("MainWindow", "I"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setToolTip(_translate("MainWindow", "Вырезать интервал"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionExit.setToolTip(_translate("MainWindow", "Выход"))
        self.actionExit.setShortcut(_translate("MainWindow", "Alt+X"))
        self.actionShowPos.setText(_translate("MainWindow", "showPos"))
        self.actionShowPos.setToolTip(_translate("MainWindow", "Показывать координаты"))
        self.actionDrawCurve.setText(_translate("MainWindow", "DrawCurve"))
        self.actionDrawCurve.setToolTip(_translate("MainWindow", "Рисование кривой"))
        self.actionApplyCurve.setText(_translate("MainWindow", "ApplyCurve"))
        self.actionApplyCurve.setToolTip(_translate("MainWindow", "Применить кривую к лучу"))
        self.actionClearCurve.setText(_translate("MainWindow", "ClearCurve"))
        self.actionClearCurve.setToolTip(_translate("MainWindow", "Удалить кривую"))
        self.actionDistance.setText(_translate("MainWindow", "distance"))
        self.actionDistance.setToolTip(_translate("MainWindow", "Измерение расстояний"))
        self.actionDistance.setShortcut(_translate("MainWindow", "D"))
        self.actionLowPassFilter.setText(_translate("MainWindow", "LowPassFilter"))
        self.actionLowPassFilter.setToolTip(_translate("MainWindow", "Частотная фильтрация сигнала"))
        self.actionScaleY.setText(_translate("MainWindow", "scaleY"))
        self.actionScaleY.setToolTip(_translate("MainWindow", "масштабировать луч на выбранном интервале"))
        self.actionRayA.setText(_translate("MainWindow", "канал 1"))
        self.actionRayA.setToolTip(_translate("MainWindow", "обрабатывать синюю кривую"))
        self.actionRayB.setText(_translate("MainWindow", "канал 2"))
        self.actionRayB.setToolTip(_translate("MainWindow", "обрабатывать зеленую кривую"))
        self.actionExp.setText(_translate("MainWindow", "exp"))
        self.actionExp.setToolTip(_translate("MainWindow", "экспоненциальное/линейное стягивание"))
        self.actionPolyfit.setText(_translate("MainWindow", "polyfit"))
        self.actionPolyfit.setToolTip(_translate("MainWindow", "Аппроксимация полиномом"))
        self.actionThinout.setText(_translate("MainWindow", "Проредить"))
        self.actionThinout.setToolTip(_translate("MainWindow", "проредить точки"))
        self.actionSave_copy_from_setup.setText(_translate("MainWindow", "Save(copy from setup)"))
        self.actionSave_copy_from_setup.setToolTip(_translate("MainWindow", "Скопировать описатель и сохранить"))
        self.actionZero.setText(_translate("MainWindow", "zero"))
        self.actionZero.setToolTip(_translate("MainWindow", "установка нуля"))
        self.actionScaleRays.setText(_translate("MainWindow", "scaleRays"))
        self.actionExchangeRays.setText(_translate("MainWindow", "exchangeRays"))

from matplotlibwidget import MatplotlibWidget
import res_rc