# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListagemProntuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMessageBox
from src.controller.prontuarioController import ProntuarioController
from src.view.prontuarioView.AtualizarProntuario import Ui_AtualizarProntuario


class Ui_ListarProntuario(object):
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
        self.txtCadastrar.setGeometry(QtCore.QRect(30, 10, 481, 51))
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
        self.listagemProntuario = QtWidgets.QTableWidget(self.frame)
        self.listagemProntuario.setGeometry(QtCore.QRect(20, 10, 591, 431))
        self.listagemProntuario.setStyleSheet("position: absolute;\n"
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
        self.listagemProntuario.setObjectName("listagemCliente")
        readProntuario = ProntuarioController.readProntuarioontroller('')
        tam = readProntuario.__len__()
        self.listagemProntuario.setColumnCount(8)
        self.listagemProntuario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listagemProntuario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listagemProntuario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemProntuario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemProntuario.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemProntuario.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemProntuario.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemProntuario.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemProntuario.setHorizontalHeaderItem(7, item)
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
        self.btnRemover = QtWidgets.QPushButton(self.container)
        self.btnRemover.setGeometry(QtCore.QRect(350, 520, 141, 61))
        self.btnRemover.setStyleSheet("position: absolute;\n"
                                      "width: 251px;\n"
                                      "height: 66px;\n"
                                      "left: 381px;\n"
                                      "top: 884px;\n"
                                      "\n"
                                      "background: #D69188;\n"
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
        self.btnRemover.setObjectName("btnRemover")
        self.btnRemover.clicked.connect(self.excluirProntuario)
        self.btnAtualizar.clicked.connect(self.AtualizarProntuario)

        self.retranslateUi(Cadastrar)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar)
        query = ProntuarioController.readProntuarioontroller('')

        while (self.listagemProntuario.rowCount() > 0):
            self.listagemProntuario.removeRow(0)
        row = 0

        while row < tam:
            self.listagemProntuario.insertRow(row)
            id = QTableWidgetItem(str(query[row][0]))
            raca = QTableWidgetItem(query[row][1])
            data = QTableWidgetItem(query[row][2])
            especie = QTableWidgetItem(query[row][3])
            porte = QTableWidgetItem(query[row][4])
            sexo = QTableWidgetItem(query[row][5])
            animal = QTableWidgetItem(str(query[row][6]))
            veterinario = QTableWidgetItem(str(query[row][7]))

            self.listagemProntuario.setItem(row, 0, id)
            self.listagemProntuario.setItem(row, 1, raca)
            self.listagemProntuario.setItem(row, 2, data)
            self.listagemProntuario.setItem(row, 3, especie)
            self.listagemProntuario.setItem(row, 4, porte)
            self.listagemProntuario.setItem(row, 5, sexo)
            self.listagemProntuario.setItem(row, 6, animal)
            self.listagemProntuario.setItem(row, 7, veterinario)

            row = row + 1

    def excluirProntuario(self):
        self.linha = self.listagemProntuario.currentIndex().row()
        idPront = self.listagemProntuario.item(self.linha, 0).text()
        self.listagemProntuario.removeRow(self.linha)
        ProntuarioController.deleteProntuarioController(idPront)

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.information)
        msg.setText("Prontuario Excluido")
        msg.setWindowTitle("Excluir Prontuario")
        # msg.setStandardB
        # uttons(QMessageBox.Ok)
        msg.exec()

    def AtualizarProntuario(self):
        self.linha = self.listagemProntuario.currentIndex().row()
        self.idprontuario = self.listagemProntuario.item(
            self.linha, 0).text()
        self.janela_prontuario_atualizar = QtWidgets.QMainWindow()
        self.janela_prontuario = Ui_AtualizarProntuario()
        self.janela_prontuario.idprontuario = self.idprontuario
        self.janela_prontuario.setupUi(self.janela_prontuario_atualizar)
        self.janela_prontuario_atualizar.show()

    def retranslateUi(self, Cadastrar):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar.setWindowTitle(_translate("Cadastrar", "Cadastrar"))
        self.healthypets.setText(_translate("Cadastrar", "HEALTHY PETS"))
        self.txtCadastrar.setText(_translate(
            "Cadastrar", "LISTAGEM DE PRONTU??RIOS"))
        item = self.listagemProntuario.horizontalHeaderItem(0)
        item.setText(_translate("Cadastrar", "ID"))
        item = self.listagemProntuario.horizontalHeaderItem(1)
        item.setText(_translate("Cadastrar", "RA??A"))
        item = self.listagemProntuario.horizontalHeaderItem(2)
        item.setText(_translate("Cadastrar", "DATA"))
        item = self.listagemProntuario.horizontalHeaderItem(3)
        item.setText(_translate("Cadastrar", "ESPECIE"))
        item = self.listagemProntuario.horizontalHeaderItem(4)
        item.setText(_translate("Cadastrar", "PORTE"))
        item = self.listagemProntuario.horizontalHeaderItem(5)
        item.setText(_translate("Cadastrar", "SEXO"))
        item = self.listagemProntuario.horizontalHeaderItem(6)
        item.setText(_translate("Cadastrar", "ID ANIMAL"))
        item = self.listagemProntuario.horizontalHeaderItem(7)
        item.setText(_translate("Cadastrar", "ID VETERIN??RIO"))
        self.btnAtualizar.setText(_translate("Cadastrar", "ATUALIZAR"))
        self.btnRemover.setText(_translate("Cadastrar", "REMOVER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastrar = QtWidgets.QWidget()
    ui = Ui_ListarProntuario()
    ui.setupUi(Cadastrar)
    Cadastrar.show()
    sys.exit(app.exec_())
