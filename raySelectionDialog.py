from qtpy.QtWidgets import *
import ui_raySelectionDialog
class raySelectionDlg(QDialog, ui_raySelectionDialog.Ui_dlgRaysSelection):
    def __init__(self, parent=None):
        super(raySelectionDlg, self).__init__(parent)
        self.setupUi(self)
        for i in range(parent.cCount):
            self.cbRay1.addItem(str(i+1))
            self.cbRay2.addItem(str(i+1))
        idx1=parent.conf.get('oscRay1', 0)
        idx2=parent.conf.get('oscRay2', 1)
        if idx1>parent.cCount:
            idx1=0
        if idx2>parent.cCount:
            idx2=1
        self.cbRay1.setCurrentIndex(idx1)
        self.cbRay2.setCurrentIndex(idx2)
        self.cbRay1.setEditable(False)
        self.cbRay2.setEditable(False)
