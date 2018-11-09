from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, qApp, QApplication, QDialog
import sys

from SolvingMethods import Euler, ImprovedEuler, RungeKutta, Exact
from inputContainer import InputContainer
from tabWindow import TabWindow



class ApplicationWindow(QDialog):

    def __init__(self):
        super(ApplicationWindow, self).__init__()

        # setting geometry
        self.setFixedSize(1000, 750)
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.mainLayout = QVBoxLayout()
        self.input_container = InputContainer()
        self.input_container.connect_clicked_btn(self.plot_data)
        self.tabWindow = TabWindow()

        self.mainLayout.addLayout(self.input_container)
        self.mainLayout.addWidget(self.tabWindow)
        self.setLayout(self.mainLayout)

    def plot_data(self):
        user_input = self.input_container.inp.is_valid_input()

        if user_input:
            terminal_n = int(user_input.pop(-1))
            method_names = ['Exact', 'Euler', 'Improved Euler', 'Runge-Kutta']

            exact = Exact(*user_input)
            e = Euler(*user_input)
            imp = ImprovedEuler(*user_input)
            r = RungeKutta(*user_input)

            methods = dict(zip(method_names, [exact, e, imp, r]))

            cur_i = self.tabWindow.currentIndex()
            for t in range(len(self.tabWindow.tabs)):
                self.tabWindow.plot_on_tabs(t, methods, terminal_n)
            self.tabWindow.setCurrentIndex((cur_i + 1) % len(self.tabWindow.tabs))
            self.tabWindow.setCurrentIndex(cur_i)






if __name__ == '__main__':
    app = QApplication(sys.argv)

    aw = ApplicationWindow()
    aw.setWindowTitle("DE solving")
    aw.show()
    sys.exit(qApp.exec_())
    # app.exec_()