import sys
import random
from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class CircleDrawer(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 400, 400)

        self.button = QtWidgets.QPushButton("Draw Circle", self)
        self.button.setGeometry(150, 20, 100, 30)
        self.button.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        x = random.randint(50, 300)
        y = random.randint(50, 300)
        diameter = random.randint(20, 100)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)


app = QtWidgets.QApplication(sys.argv)
window = CircleDrawer()
window.show()
sys.exit(app.exec())
