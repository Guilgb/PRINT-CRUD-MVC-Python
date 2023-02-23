from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from src.view.animalView.AtualizarAnimal import AtualizarAnimal
from src.view.animalView.ListagemAnimais import ListarAnimais
import sys


class Botoes(object):
    # botão ALUGUEL CLICK #
    def Animal_Click():
        frmAnimal = QtWidgets.QApplication(sys.argv)
        Cadastrar = QtWidgets.QWidget()
        ui = AtualizarAnimal()
        ui.setupUi(Cadastrar)
        Cadastrar.show()
        sys.exit(frmAnimal.exec())

    def ListarAnimal_Click():
        frmAnimal = QtWidgets.QApplication(sys.argv)
        Cadastrar = QtWidgets.QWidget()
        ui = ListarAnimais()
        ui.setupUi(Cadastrar)
        Cadastrar.show()
        sys.exit(frmAnimal.exec())
