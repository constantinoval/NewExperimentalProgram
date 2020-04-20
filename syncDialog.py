from qtpy.QtCore import *
from qtpy.QtWidgets import *
from qtpy.QtGui import *
from qtpy import uic
from matplotlib.backends.backend_qt5agg import FigureCanvas as Canvas
from matplotlib.figure import Figure
from myNavigation import *
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavTB
from odbcAccess import unpackTable
from itertools import cycle
import numpy as np
from copy import deepcopy

pulses_cycle = cycle([0, 1, 2])
pulses_names = ['I', 'R', 'T']


class MatplotlibWidget(Canvas):
    def __init__(self, parent=None):
        figure = Figure(figsize=(4, 3))
        self.ax = figure.add_subplot(111)
        Canvas.__init__(self, figure)
        c = Canvas(Figure())
        self.setParent(parent)
        Canvas.setSizePolicy(self, QSizePolicy.Expanding,
                             QSizePolicy.Expanding)
        Canvas.updateGeometry(self)
        self.figure = figure
        self.ax.grid()
        self.tb = NavTB(self.figure.canvas, self)
        self.tb.hide()
        self.nav = MyNavigation(self.ax, mplwidget=self)
        self.figure.subplots_adjust(right=0.98, top=0.98)
        self.lines = []


class MySyncDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('syncDialog.ui', self)
        self.parent = parent
        self.mpl = MatplotlibWidget(self)
        self.mplLayout.addWidget(self.mpl)
        self.pulses = unpackTable(parent.odbc.getExperimentData(
            parent.exp_code_to_sync)['ИмпульсыОбработанные'])
        self.sync_pulses = list(unpackTable(parent.odbc.getExperimentData(
            parent.exp_code_to_sync)['ИмпульсыОбработанные']))
        self.mpl.ax.set_title('I')
        self.n_points = len(self.pulses[0])
        self.lines = []
        self.deltas = [0, 0, 0]
        self.active_pulse = next(pulses_cycle)
        self.updateMpl()
        self.mpl.figure.tight_layout()
        self.installEventFilter(self)

    def updateMpl(self):
        if not self.lines:
            l1, = self.mpl.ax.plot(self.pulses[0]*1e6, self.pulses[1][0])
            l2, = self.mpl.ax.plot(self.pulses[0]*1e6, self.pulses[1][1])
            l3, = self.mpl.ax.plot(self.pulses[0]*1e6, self.pulses[1][2])
            l4, = self.mpl.ax.plot(self.pulses[0]*1e6,
                                   self.pulses[1][0]-self.pulses[1][1], '--k')
            self.lines = [l1, l2, l3, l4]
            y0, y1 = self.mpl.ax.get_ylim()
            self.dy = y1-y0
    # def keyPressEvent(self, event):
    #     print(event.key(), event.modifiers())
    #     if event.key() == Qt.Key_Up:
    #         print('Up')
    #         event.accept()
    #     super(MySyncDialog, self).keyPressEvent(event)

    def eventFilter(self, obj, ev):
        if ev.type() == QEvent.KeyPress:
            if ev.key() == Qt.Key_Tab:  # and ev.modifiers() == Qt.ControlModifier:
                self.change_active_pulse()
            if ev.key() == Qt.Key_Left and ev.modifiers() == Qt.ShiftModifier:
                self.shift(-1)
            if ev.key() == Qt.Key_Right and ev.modifiers() == Qt.ShiftModifier:
                self.shift(1)
            if ev.key() == Qt.Key_Left and ev.modifiers() == Qt.NoModifier:
                self.shift(-self.n_points//100)
            if ev.key() == Qt.Key_Right and ev.modifiers() == Qt.NoModifier:
                self.shift(self.n_points//100)
            if ev.key() == Qt.Key_Left and ev.modifiers() == Qt.ControlModifier:
                self.shiftall(-self.n_points//100)
            if ev.key() == Qt.Key_Right and ev.modifiers() == Qt.ControlModifier:
                self.shiftall(self.n_points//100)
            if ev.key() == Qt.Key_Left and ev.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier):
                self.shiftall(-1)
            if ev.key() == Qt.Key_Right and ev.modifiers() == (Qt.ControlModifier | Qt.ShiftModifier):
                self.shiftall(1)
            if ev.key() == Qt.Key_Return:
                self.accept()
            if ev.key() == Qt.Key_Escape:
                self.reject()
            if ev.key() == Qt.Key_Up and ev.modifiers() == Qt.NoModifier:
                self.v_shift(self.dy/100.)
            if ev.key() == Qt.Key_Down and ev.modifiers() == Qt.NoModifier:
                self.v_shift(-self.dy/100.)
            if ev.key() == Qt.Key_Up and ev.modifiers() == Qt.ShiftModifier:
                self.v_shift(self.dy/1000.)
            if ev.key() == Qt.Key_Down and ev.modifiers() == Qt.ShiftModifier:
                self.v_shift(-self.dy/1000.)
            return True
        return False

    def change_active_pulse(self):
        self.active_pulse = next(pulses_cycle)
        self.mpl.ax.set_title(pulses_names[self.active_pulse])
        self.mpl.figure.canvas.draw_idle()

    def shift(self, delta=1):
        i = self.active_pulse
        self.deltas[i] += delta
        self.updatePulses([i])

    def v_shift(self, delta=1e-4):
        i = self.active_pulse
        new_data = self.lines[i].get_ydata()+delta
        self.lines[i].set_ydata(new_data)
        self.lines[3].set_ydata(
            self.lines[0].get_ydata()-self.lines[1].get_ydata())
        self.sync_pulses[1][i] = new_data
        self.pulses[1][i] = new_data
        self.mpl.figure.canvas.draw_idle()
        y0, y1 = self.mpl.ax.get_ylim()
        self.dy = y1-y0
        self.updateDiagramm()

    def shiftall(self, delta=1):
        for i in range(3):
            self.deltas[i] += delta
        self.updatePulses(range(3))

    def updatePulses(self, ii):
        xx = np.arange(self.n_points)
        for i in ii:
            new_data = np.interp(xx, xx+self.deltas[i], self.pulses[1][i])
            self.lines[i].set_ydata(new_data)
            self.sync_pulses[1][i] = new_data
        self.lines[3].set_ydata(
            self.lines[0].get_ydata()-self.lines[1].get_ydata())
        self.mpl.figure.canvas.draw_idle()
        self.updateDiagramm()

    def updateDiagramm(self):
        rez = self.parent.calculateDiagram(
            self.parent.exp_code_to_sync, pulses=self.sync_pulses)
        for i, l in enumerate(self.parent.lines):
            if l:
                l.set_xdata(rez[self.parent.idxs[0]])
                l.set_ydata(rez[self.parent.idxs[1+i]])
        self.parent.mplComparDiag.figure.canvas.draw_idle()
