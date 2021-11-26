import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from pyqt5.meugerador import gera_pcf2
from pyqt5.validandocpf import validacpf2
import geradordecpf


class GeraValidaCPF(QMainWindow, geradordecpf.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btGera.clicked.connect(self.gera_cpf)
        self.btValida.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.retornoGera.setText(
            str(gera_pcf2()))

    def valida_cpf(self):
        cpf = self.retornoGera.text()
        self.retorno.setText(
            str(validacpf2(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida_pcf = GeraValidaCPF()
    gera_valida_pcf.show()
    qt.exec_()
