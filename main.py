from PyQt5 import QtCore, QtGui, QtWidgets, uic
translate = QtCore.QCoreApplication.translate
from MainWindowF import Ui_MainWindow
import sys
import resource

class CamBox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        uic.loadUi('Frame.ui', self)
        return

stylesheet = """
    QFrame#frame {
        background-color: rgb(255, 255, 255); 
        border: 1px inset black;
    }
"""


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #uic.loadUi('MainWindow.ui', self)
        self.setupUi(self)
        self.boxes = list()
        for i in range(10):
            self.boxes.append(CamBox(self))
            self.gridLayout.addWidget(self.boxes[i])


def main():
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    main_ = MainWindow()
    main_.show()
    app.exec_()
    print("main() end")
    return


if __name__ == "__main__":
    main()
