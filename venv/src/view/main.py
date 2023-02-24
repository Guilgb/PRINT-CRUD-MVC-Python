from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from src.view.animalView.AtualizarAnimal import AtualizarAnimal
from src.view.animalView.ListagemAnimais import ListarAnimais
import sys


class Botoes(object):
    def Animal_Click():
        frmAnimal = QtWidgets.QMainWindow()
        ui = AtualizarAnimal()
        ui.setupUi(frmAnimal)
        frmAnimal.show()

    def ListarAnimal_Click():
        frmAnimal = QtWidgets.QMainWindow()
        ui = ListarAnimais()
        ui.setupUi(frmAnimal)
        frmAnimal.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastrar = QtWidgets.QWidget()
    ui = Botoes()
    ui.setupUi(Cadastrar)
    Cadastrar.show()
    sys.exit(app.exec())
