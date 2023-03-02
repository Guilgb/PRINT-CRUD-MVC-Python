from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.view.viewVacina.cadastrarVacina import CRUDVacina
import sys


class Botoes(object):
    def Listavacina(self):
        self.janela_vacina = QtWidgets.QMainWindow()
        self.vacinaJanela = CRUDVacina()
        self.vacinaJanela.setupUi(self.janela_vacina)
        self.janela_vacina.show()


Botoes.vacina('')
