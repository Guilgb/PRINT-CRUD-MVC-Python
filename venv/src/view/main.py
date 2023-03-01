from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.view.animalView.CadastrarAnimal import CadastrarAnimais
from src.view.animalView.ListagemAnimais import ListarAnimais
import sys


class Botoes(object):
    def Animal_Click():
        app = QtWidgets.QApplication(sys.argv)
        frmAnimal = QtWidgets.QMainWindow()
        ui = CadastrarAnimais()
        ui.setupUi(frmAnimal)
        frmAnimal.show()
        sys.exit(app.exec())

    def ListarAnimal_Click():
        a = CadastrarAnimais()
        app = QtWidgets.QApplication(sys.argv)
        frmAnimal = QtWidgets.QMainWindow()
        frmAnimal.setWindowFlags(frmAnimal.windowFlags())
        ui = ListarAnimais()
        ui.setupUi(frmAnimal)
        frmAnimal.show()
        sys.exit(app.exec())


Botoes.Animal_Click()
