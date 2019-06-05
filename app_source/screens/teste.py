import sys

from PyQt5 import QtWidgets

from main_window import Ui_MainWindow  # importing our generated file


class myWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = myWindow()
application.show()
sys.exit(app.exec())
