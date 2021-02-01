from PyQt5 import QtCore, QtGui, QtWidgets, uic
from slide_test import Ui_MainWindow
import sys
translate = QtCore.QCoreApplication.translate


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # uic.loadUi('MainWindow.ui', self)
        self.setupUi(self)
        self.horizontalSlider.hover_event.connect(lambda e: self.slide_event("hover", e))
        self.horizontalSlider.valueChanged.connect(lambda e: self.slide_event("change", e))
        print()

    def slide_event(self, typ, event):
        print(f"{typ} event", event)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_ = MainWindow()
    main_.show()
    app.exec_()
    print("main() end")
    return


if __name__ == "__main__":
    main()
