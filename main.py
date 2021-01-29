from PyQt5 import QtCore, QtGui, QtWidgets, uic
translate = QtCore.QCoreApplication.translate
import sys
import resource

class CamBox(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        uic.loadUi('Frame.ui', self)
        return

stylesheet = """
    QFrame#Frame {
        background-color: rgb(255, 255, 255); 
        border: 1px inset black;
    }
"""



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('MainWindow.ui', self)
        self.boxes = list()
        for i in range(10):
            self.boxes.append(CamBox(self))
            self.gridLayout.addWidget(self.boxes[i], i//3, i%3)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(stylesheet)
    main = MainWindow()
    main.show()
    app.exec_()
    print("main() end")
    return

if __name__ == "__main__":
    main()