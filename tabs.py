from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Tab(QWidget):
    def __init__(self, parent: QTabWidget):
        super(Tab, self).__init__()
        self.initUI(parent)

    def initUI(self, parent: QWidget):
        box = QVBoxLayout()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.toolbar = NavigationToolbar(self.canvas, parent)
        box.addWidget(self.toolbar)
        box.addWidget(self.canvas)
        self.setLayout(box)