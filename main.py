from PyQt5 import QtCore, QtGui, QtWidgets, uic
translate = QtCore.QCoreApplication.translate
from slide_test import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # uic.loadUi('MainWindow.ui', self)
        self.setupUi(self)
        self.horizontalSlider.hover.connect(lambda e: self.hover_event(e))

    def hover_event(self, event):
        print("hover", event)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_ = MainWindow()
    main_.show()
    app.exec_()
    print("main() end")
    return


if __name__ == "__main__":
    main()
