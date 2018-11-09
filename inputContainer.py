from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QLabel, QLineEdit


class InputContainer(QHBoxLayout):
    def __init__(self):
        super(QHBoxLayout, self).__init__()

        self.input_variables = ['x0', 'y0', 'xN', 'N', 'N terminal']
        self.initUI()


    def initUI(self):
        self.inp = InputVariables(names=self.input_variables)
        self.addStretch(2)
        self.inp.fill_container(self)
        self.plot_btn = QPushButton('Plot')
        self.addWidget(self.plot_btn)

    def connect_clicked_btn(self, func):
        self.plot_btn.clicked.connect(func)


class InputVariables:
    def __init__(self, names):
        self.names = names
        self.input_buttons = []
        for v in self.names:
            self.input_buttons.append(InputButton(title=v + ' ='))

    def fill_container(self, parent: QHBoxLayout):
        values = ['1', '3', '4', '100', '100']
        for b in zip(self.input_buttons, values):
            b[0].lineEdit.setText(b[1])
            b[0].add_to_container(parent)

    def is_valid_input(self):
        inp = []
        for i in self.input_buttons:
            a = i.lineEdit.text()
            if not a:
                return False
            try:
                inp.append(float(a))
            except ValueError:
                return False
        return inp

class InputButton:
    def __init__(self, title: str):
        self.inputField = QLabel(title)
        self.lineEdit = QLineEdit()
        # self.inputField.setFixedWidth(50)
        self.lineEdit.setFixedWidth(50)

    def add_to_container(self, parent: QHBoxLayout):
        parent.addWidget(self.inputField)
        parent.addWidget(self.lineEdit)
        parent.addStretch(1)
