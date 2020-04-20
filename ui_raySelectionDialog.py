# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'raySelectionDialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from qtpy import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_dlgRaysSelection(object):
    def setupUi(self, dlgRaysSelection):
        dlgRaysSelection.setObjectName(_fromUtf8("dlgRaysSelection"))
        dlgRaysSelection.setWindowModality(QtCore.Qt.WindowModal)
        dlgRaysSelection.resize(174, 75)
#        sizePolicy = QtWidgets.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
#        sizePolicy.setHorizontalStretch(0)
#        sizePolicy.setVerticalStretch(0)
#        sizePolicy.setHeightForWidth(dlgRaysSelection.sizePolicy().hasHeightForWidth())
#        dlgRaysSelection.setSizePolicy(sizePolicy)
        dlgRaysSelection.setMaximumSize(QtCore.QSize(174, 75))
        dlgRaysSelection.setSizeGripEnabled(False)
        dlgRaysSelection.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlgRaysSelection)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cbRay1 = QtWidgets.QComboBox(dlgRaysSelection)
        self.cbRay1.setObjectName(_fromUtf8("cbRay1"))
        self.horizontalLayout.addWidget(self.cbRay1)
        self.cbRay2 = QtWidgets.QComboBox(dlgRaysSelection)
        self.cbRay2.setObjectName(_fromUtf8("cbRay2"))
        self.horizontalLayout.addWidget(self.cbRay2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(dlgRaysSelection)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(dlgRaysSelection)
        self.buttonBox.accepted.connect(dlgRaysSelection.accept)
        self.buttonBox.rejected.connect(dlgRaysSelection.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgRaysSelection)

    def retranslateUi(self, dlgRaysSelection):
        dlgRaysSelection.setWindowTitle(_translate("dlgRaysSelection", "Dialog", None))

