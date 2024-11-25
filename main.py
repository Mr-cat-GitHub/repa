import sys
import random
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.add_circle)
        self.circles = []

    def add_circle(self):
        x = random.randint(50, 300)
        y = random.randint(50, 300)
        diameter = random.randint(20, 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, diameter in self.circles:
            painter.setBrush(QColor("purple"))
            painter.drawEllipse(x, y, diameter, diameter)


app = QtWidgets.QApplication(sys.argv)
window = CircleDrawer()
window.show()
sys.exit(app.exec())
