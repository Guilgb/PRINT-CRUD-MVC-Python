from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from src.controller.animalController import AnimalController


class Ui_ListarAnimalProntuario(object):
    def setupUi(self, Cadastrar):
        Cadastrar.setObjectName("Cadastrar")
        Cadastrar.resize(900, 600)
        Cadastrar.setMinimumSize(QtCore.QSize(900, 240))
        Cadastrar.setMaximumSize(QtCore.QSize(900, 600))
        self.navegation = QtWidgets.QFrame(Cadastrar)
        self.navegation.setGeometry(QtCore.QRect(0, 0, 221, 741))
        self.navegation.setStyleSheet("background-color: rgb(48, 68, 86)")
        self.navegation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navegation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navegation.setObjectName("navegation")
        self.healthypets = QtWidgets.QPushButton(self.navegation)
        self.healthypets.setEnabled(False)
        self.healthypets.setGeometry(QtCore.QRect(0, 0, 221, 111))
        self.healthypets.setAccessibleName("")
        self.healthypets.setAutoFillBackground(False)
        self.healthypets.setStyleSheet("background-color: rgb(91, 113, 133);\n"
                                       "color: white;")
        self.healthypets.setObjectName("healthypets")
        self.container = QtWidgets.QFrame(Cadastrar)
        self.container.setGeometry(QtCore.QRect(220, 0, 920, 600))
        self.container.setMinimumSize(QtCore.QSize(920, 600))
        self.container.setMaximumSize(QtCore.QSize(920, 740))
        self.container.setStyleSheet("background-color:rgb(201, 201, 201)")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.txtCadastrar = QtWidgets.QLabel(self.container)
        self.txtCadastrar.setGeometry(QtCore.QRect(30, 10, 401, 51))
        self.txtCadastrar.setStyleSheet("position: absolute;\n"
                                        "width: 397px;\n"
                                        "height: 36px;\n"
                                        "left: 299px;\n"
                                        "top: 80px;\n"
                                        "\n"
                                        "font-family: \'Inter\';\n"
                                        "font-style: normal;\n"
                                        "font-weight: 600;\n"
                                        "font-size: 32px;\n"
                                        "line-height: 39px;\n"
                                        "text-align: center;\n"
                                        "\n"
                                        "color: white;\n"
                                        "")
        self.txtCadastrar.setObjectName("txtCadastrar")
        self.frame = QtWidgets.QFrame(self.container)
        self.frame.setGeometry(QtCore.QRect(20, 60, 621, 451))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listagemAnimal = QtWidgets.QTableWidget(self.frame)
        self.listagemAnimal.setGeometry(QtCore.QRect(20, 10, 591, 431))
        self.listagemAnimal.setStyleSheet("position: absolute;\n"
                                          "width: 397px;\n"
                                          "height: 36px;\n"
                                          "left: 299px;\n"
                                          "top: 80px;\n"
                                          "background-color:rgb(201, 201, 201);\n"
                                          "\n"
                                          "font-family: \'Inter\';\n"
                                          "font-style: normal;\n"
                                          "font-weight: 100;\n"
                                          "font-size:12px;\n"
                                          "line-height: 39px;\n"
                                          "text-align: center;\n"
                                          "\n"
                                          "color: black;")
        self.listagemAnimal.setObjectName("listagemCliente")
        readAnimal = AnimalController.readControllerAimal('')
        tam = readAnimal.__len__()
        self.listagemAnimal.setColumnCount(8)
        self.listagemAnimal.setRowCount(tam)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listagemAnimal.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listagemAnimal.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemAnimal.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemAnimal.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemAnimal.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemAnimal.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemAnimal.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemAnimal.setHorizontalHeaderItem(7, item)
        self.btnAtualizar = QtWidgets.QPushButton(self.container)
        self.btnAtualizar.setGeometry(QtCore.QRect(500, 520, 141, 61))
        self.btnAtualizar.setStyleSheet("position: absolute;\n"
                                        "width: 251px;\n"
                                        "height: 66px;\n"
                                        "left: 381px;\n"
                                        "top: 884px;\n"
                                        "\n"
                                        "background: #304456;\n"
                                        "border-radius: 27px;\n"
                                        "\n"
                                        "font-family: \'Inter\';\n"
                                        "font-style: normal;\n"
                                        "font-weight: 700;\n"
                                        "font-size: 20px;\n"
                                        "line-height: 24px;\n"
                                        "text-align: center;\n"
                                        "\n"
                                        "color: #FFFFFF;")
        self.btnAtualizar.setObjectName("btnAtualizar")

        self.retranslateUi(Cadastrar)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar)
        query = AnimalController.readControllerAimal('')

        while (self.listagemAnimal.rowCount() > 0):
            self.listagemAnimal.removeRow(0)
        row = 0
        while row < tam:
            self.listagemAnimal.insertRow(row)
            idAnimal = QTableWidgetItem(str(query[row][0]))
            nomeAnimal = QTableWidgetItem(query[row][1])
            idade = QTableWidgetItem(query[row][6])
            sexo = QTableWidgetItem(query[row][3])
            raca = QTableWidgetItem(query[row][4])
            peso = QTableWidgetItem(query[row][5])
            dono = QTableWidgetItem(query[row][7])
            especie = QTableWidgetItem(query[row][2])

            self.listagemAnimal.setItem(row, 0, idAnimal)
            self.listagemAnimal.setItem(row, 1, nomeAnimal)
            self.listagemAnimal.setItem(row, 2, idade)
            self.listagemAnimal.setItem(row, 3, sexo)
            self.listagemAnimal.setItem(row, 4, raca)
            self.listagemAnimal.setItem(row, 5, peso)
            self.listagemAnimal.setItem(row, 6, especie)
            self.listagemAnimal.setItem(row, 7, dono)

            row = row + 1

    def SelecionarAnimal(self):
        self.linha = self.listagemAnimal.currentIndex().row()
        self.idAnimal = self.listagemAnimal.item(self.linha, 0).text()
        return self.idAnimal

    def retranslateUi(self, Cadastrar):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar.setWindowTitle(_translate("Cadastrar", "Cadastrar"))
        self.healthypets.setText(_translate("Cadastrar", "HEALTHY PETS"))
        self.txtCadastrar.setText(_translate(
            "Cadastrar", "LISTAGEM DE ANIMAIS"))
        item = self.listagemAnimal.horizontalHeaderItem(0)
        item.setText(_translate("Cadastrar", "ID"))
        item = self.listagemAnimal.horizontalHeaderItem(1)
        item.setText(_translate("Cadastrar", "NOME"))
        item = self.listagemAnimal.horizontalHeaderItem(2)
        item.setText(_translate("Cadastrar", "IDADE"))
        item = self.listagemAnimal.horizontalHeaderItem(3)
        item.setText(_translate("Cadastrar", "SEXO"))
        item = self.listagemAnimal.horizontalHeaderItem(4)
        item.setText(_translate("Cadastrar", "RACA"))
        item = self.listagemAnimal.horizontalHeaderItem(5)
        item.setText(_translate("Cadastrar", "PESO"))
        item = self.listagemAnimal.horizontalHeaderItem(6)
        item.setText(_translate("Cadastrar", "DONO"))
        item = self.listagemAnimal.horizontalHeaderItem(7)
        item.setText(_translate("Cadastrar", "RACAO"))
        self.btnAtualizar.setText(_translate("Cadastrar", "SELECIONAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastrar = QtWidgets.QWidget()
    ui = Ui_ListarAnimalProntuario()
    ui.setupUi(Cadastrar)
    Cadastrar.show()
    sys.exit(app.exec_())
