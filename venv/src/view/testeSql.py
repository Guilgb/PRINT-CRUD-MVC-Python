from PyQt5 import uic, QtWidgets


def insert():
    print('nada')


app = QtWidgets.QApplication([])
tela = uic.loadUi("cadastrarCliente.ui")

tela.show()
app.exec()
