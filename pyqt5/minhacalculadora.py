import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout, QLineEdit
import minhacalc


class MinhaCalculadora(QMainWindow, minhacalc.Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn1.clicked.connect(self.btnone)
        self.btn2.clicked.connect(self.btntwo)
        self.btn3.clicked.connect(self.btnthree)
        self.btn4.clicked.connect(self.btnfour)
        self.btn5.clicked.connect(self.btnfive)
        self.btn6.clicked.connect(self.btnsix)
        self.btn7.clicked.connect(self.btnseven)
        self.btn8.clicked.connect(self.btneight)
        self.btn9.clicked.connect(self.btnnine)
        self.btnmais.clicked.connect(self.sinaladic)
        self.pushButton_19.clicked.connect(self.sinaligual)
        self.btnback.clicked.connect(self.back)
        self.btnc.clicked.connect(self.clear)
        self.btnmenos.clicked.connect(self.sinalsub)
        self.btnmult.clicked.connect(self.sinalmultp)
        self.btndiv.clicked.connect(self.sinaldiv)
        self.pushButton_6.clicked.connect(self.btnzero)
        self.pushButton_5.clicked.connect(self.btnponto)

    def btnone(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '1')

    def btntwo(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '2')

    def btnthree(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '3')

    def btnfour(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '4')

    def btnfive(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '5')

    def btnsix(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '6')

    def btnseven(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '7')

    def btneight(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '8')

    def btnnine(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '9')

    def btnzero(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '0')

    def sinaladic(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '+')

    def sinalsub(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '-')

    def sinalmultp(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '*')

    def sinaldiv(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '/')

    def back(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text[:len(text)-1])

    def clear(self):
        self.lineEdit.setText("")

    def btnponto(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text + '.')

    def sinaligual(self):
        try:
            self.lineEdit.setText(
                str(eval(self.lineEdit.text()))
            )
        except Exception as e:
            self.lineEdit.setText('Conta inválida!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    minhacalculadora = MinhaCalculadora()
    minhacalculadora.show()
    qt.exec_()
