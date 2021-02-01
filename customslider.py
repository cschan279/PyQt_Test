from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QEvent


class CustomSlider(QtWidgets.QSlider):
    hover_event = QtCore.pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_Hover)
        self.pos = -1

    def event(self, event):
        if event.type() in [QEvent.HoverEnter, QEvent.HoverLeave, QEvent.HoverMove]:
            value = self.get_value_from_pos(event.pos().x())
            self.hover_event.emit(value)
        return super().event(event)

    def get_value_from_pos(self, pos):
        range = self.maximum() - self.minimum()
        value = (pos / self.width()) * range + self.minimum()
        return value

    def mousePressEvent(self, ev):
        """ Jump to click position """
        self.setValue(self.get_value_from_pos(ev.x()))
        return

    def mouseMoveEvent(self, ev):
        """ Jump to click position """
        self.setValue(self.get_value_from_pos(ev.x()))
        return
