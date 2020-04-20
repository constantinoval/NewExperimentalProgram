# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scaleRaysDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dScaleRays(object):
    def setupUi(self, dScaleRays):
        dScaleRays.setObjectName(_fromUtf8("dScaleRays"))
        dScaleRays.setWindowModality(QtCore.Qt.WindowModal)
        dScaleRays.resize(264, 90)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dScaleRays.sizePolicy().hasHeightForWidth())
        dScaleRays.setSizePolicy(sizePolicy)
        dScaleRays.setModal(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(dScaleRays)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(dScaleRays)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.dsbRay1Scale = QtGui.QDoubleSpinBox(dScaleRays)
        self.dsbRay1Scale.setDecimals(6)
        self.dsbRay1Scale.setMaximum(100.0)
        self.dsbRay1Scale.setSingleStep(0.1)
        self.dsbRay1Scale.setProperty("value", 1.0)
        self.dsbRay1Scale.setObjectName(_fromUtf8("dsbRay1Scale"))
        self.verticalLayout.addWidget(self.dsbRay1Scale)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_2 = QtGui.QLabel(dScaleRays)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.dsbRay2Scale = QtGui.QDoubleSpinBox(dScaleRays)
        self.dsbRay2Scale.setDecimals(6)
        self.dsbRay2Scale.setMaximum(100.0)
        self.dsbRay2Scale.setSingleStep(0.1)
        self.dsbRay2Scale.setProperty("value", 1.0)
        self.dsbRay2Scale.setObjectName(_fromUtf8("dsbRay2Scale"))
        self.verticalLayout_2.addWidget(self.dsbRay2Scale)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(dScaleRays)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(dScaleRays)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dScaleRays.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dScaleRays.reject)
        QtCore.QMetaObject.connectSlotsByName(dScaleRays)

    def retranslateUi(self, dScaleRays):
        dScaleRays.setWindowTitle(_translate("dScaleRays", "Dialog", None))
        self.label.setText(_translate("dScaleRays", "Ray 1", None))
        self.label_2.setText(_translate("dScaleRays", "Ray 2", None))

