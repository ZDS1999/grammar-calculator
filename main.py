# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from form import Ui_Form
from grammar import Expression


class Calculator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.expr = ''

        for btn in self.ui.inputTokens.buttons():
            btn.clicked.connect(self.add_char)

        self.ui.btn_equal.clicked.connect(self.equals)

        self.show()

    def add_char(self):
        content = self.sender().objectName().split('_')[1]
        if str.isdigit(content):
            self.expr += content
        elif content == 'lp':
            self.expr += '('
        elif content == 'rp':
            self.expr += ')'
        elif content == 'mul':
            self.expr += '*'
        elif content == 'div':
            self.expr += '/'
        elif content == 'add':
            self.expr += '+'
        elif content == 'sub':
            self.expr += '-'
        elif content == 'dot':
            self.expr += '.'
        elif content == 'bs':
            leng = len(self.expr)
            self.expr = self.expr[:leng-1:]
        elif content == 'clear':
            self.expr = ''
        else:
            print('should never come here!')
            sys.exit(1)
        self.ui.lineEdit.setText(self.expr)

    def equals(self):
        self.expr += '$'
        expression = Expression(self.expr)
        self.expr = str(expression.start())
        self.ui.lineEdit.setText(self.expr)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    cal = Calculator()
    sys.exit(app.exec_())
