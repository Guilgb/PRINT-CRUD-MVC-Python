# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CadastrarAnimal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
from src.model.animal import Animal
from src.controller.animalController import AnimalController
from src.view.animalView.ListagemAnimais import ListarAnimais
from src.view.clienteView.ListarCliente import ListarCliente
from src.view.animalView.ListaClienteAnimal import ListaClienteAnimal


class Ui_CadastrarAnimal(object):
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
        self.txtCadastrar.setGeometry(QtCore.QRect(30, 10, 291, 51))
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
        self.frame.setGeometry(QtCore.QRect(20, 60, 621, 401))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nomeAnimal = QtWidgets.QLabel(self.frame)
        self.nomeAnimal.setGeometry(QtCore.QRect(30, 30, 171, 21))
        self.nomeAnimal.setStyleSheet("position: absolute;\n"
                                      "width: 184px;\n"
                                      "height: 24px;\n"
                                      "left: 420px;\n"
                                      "top: 277px;\n"
                                      "\n"
                                      "font-family: \'Inter\';\n"
                                      "font-style: normal;\n"
                                      "font-weight: 300;\n"
                                      "font-size: 20px;\n"
                                      "line-height: 24px;\n"
                                      "text-align: center;\n"
                                      "\n"
                                      "color: #000000;")
        self.nomeAnimal.setObjectName("nomeAnimal")
        self.porte = QtWidgets.QLabel(self.frame)
        self.porte.setGeometry(QtCore.QRect(30, 174, 71, 31))
        self.porte.setStyleSheet("position: absolute;\n"
                                 "width: 184px;\n"
                                 "height: 24px;\n"
                                 "left: 420px;\n"
                                 "top: 277px;\n"
                                 "\n"
                                 "font-family: \'Inter\';\n"
                                 "font-style: normal;\n"
                                 "font-weight: 300;\n"
                                 "font-size: 20px;\n"
                                 "line-height: 24px;\n"
                                 "text-align: center;\n"
                                 "\n"
                                 "color: #000000;")
        self.porte.setObjectName("porte")
        self.raca = QtWidgets.QLabel(self.frame)
        self.raca.setGeometry(QtCore.QRect(30, 130, 51, 21))
        self.raca.setStyleSheet("position: absolute;\n"
                                "width: 184px;\n"
                                "height: 24px;\n"
                                "left: 420px;\n"
                                "top: 277px;\n"
                                "\n"
                                "font-family: \'Inter\';\n"
                                "font-style: normal;\n"
                                "font-weight: 300;\n"
                                "font-size: 20px;\n"
                                "line-height: 24px;\n"
                                "text-align: center;\n"
                                "\n"
                                "color: #000000;")
        self.raca.setObjectName("raca")
        self.racao = QtWidgets.QLabel(self.frame)
        self.racao.setGeometry(QtCore.QRect(329, 231, 61, 21))
        self.racao.setStyleSheet("position: absolute;\n"
                                 "width: 184px;\n"
                                 "height: 24px;\n"
                                 "left: 420px;\n"
                                 "top: 277px;\n"
                                 "\n"
                                 "font-family: \'Inter\';\n"
                                 "font-style: normal;\n"
                                 "font-weight: 300;\n"
                                 "font-size: 20px;\n"
                                 "line-height: 24px;\n"
                                 "text-align: center;\n"
                                 "\n"
                                 "color: #000000;")
        self.racao.setObjectName("racao")
        self.status = QtWidgets.QLabel(self.frame)
        self.status.setGeometry(QtCore.QRect(320, 183, 71, 16))
        self.status.setStyleSheet("position: absolute;\n"
                                  "width: 184px;\n"
                                  "height: 24px;\n"
                                  "left: 420px;\n"
                                  "top: 277px;\n"
                                  "\n"
                                  "font-family: \'Inter\';\n"
                                  "font-style: normal;\n"
                                  "font-weight: 300;\n"
                                  "font-size: 20px;\n"
                                  "line-height: 24px;\n"
                                  "text-align: center;\n"
                                  "\n"
                                  "color: #000000;")
        self.status.setObjectName("status")
        self.tutor = QtWidgets.QLabel(self.frame)
        self.tutor.setGeometry(QtCore.QRect(30, 281, 141, 20))
        self.tutor.setStyleSheet("position: absolute;\n"
                                 "width: 184px;\n"
                                 "height: 24px;\n"
                                 "left: 420px;\n"
                                 "top: 277px;\n"
                                 "\n"
                                 "font-family: \'Inter\';\n"
                                 "font-style: normal;\n"
                                 "font-weight: 300;\n"
                                 "font-size: 20px;\n"
                                 "line-height: 24px;\n"
                                 "text-align: center;\n"
                                 "\n"
                                 "color: #000000;")
        self.tutor.setObjectName("tutor")
        self.tipo = QtWidgets.QLabel(self.frame)
        self.tipo.setGeometry(QtCore.QRect(400, 75, 51, 21))
        self.tipo.setStyleSheet("position: absolute;\n"
                                "width: 184px;\n"
                                "height: 24px;\n"
                                "left: 420px;\n"
                                "top: 277px;\n"
                                "\n"
                                "font-family: \'Inter\';\n"
                                "font-style: normal;\n"
                                "font-weight: 300;\n"
                                "font-size: 20px;\n"
                                "line-height: 24px;\n"
                                "text-align: center;\n"
                                "\n"
                                "color: #000000;")
        self.tipo.setObjectName("tipo")
        self.campoNomeAnimal = QtWidgets.QTextEdit(self.frame)
        self.campoNomeAnimal.setGeometry(QtCore.QRect(210, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoNomeAnimal.setFont(font)
        self.campoNomeAnimal.setStyleSheet("position: absolute;\n"
                                           "width: 692px;\n"
                                           "height: 51px;\n"
                                           "left: 625px;\n"
                                           "top: 264px;\n"
                                           "\n"
                                           "background: #D9D9D9;\n"
                                           "border-radius: 8px;")
        self.campoNomeAnimal.setObjectName("campoNomeAnimal")
        self.campoRaca = QtWidgets.QTextEdit(self.frame)
        self.campoRaca.setGeometry(QtCore.QRect(100, 120, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoRaca.setFont(font)
        self.campoRaca.setStyleSheet("position: absolute;\n"
                                     "width: 692px;\n"
                                     "height: 51px;\n"
                                     "left: 625px;\n"
                                     "top: 264px;\n"
                                     "\n"
                                     "background: #D9D9D9;\n"
                                     "border-radius: 8px;")
        self.campoRaca.setObjectName("campoRaca")
        self.campoPorte = QtWidgets.QTextEdit(self.frame)
        self.campoPorte.setGeometry(QtCore.QRect(100, 170, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoPorte.setFont(font)
        self.campoPorte.setStyleSheet("position: absolute;\n"
                                      "width: 692px;\n"
                                      "height: 51px;\n"
                                      "left: 625px;\n"
                                      "top: 264px;\n"
                                      "\n"
                                      "background: #D9D9D9;\n"
                                      "border-radius: 8px;")
        self.campoPorte.setObjectName("campoPorte")
        self.campoRacao = QtWidgets.QTextEdit(self.frame)
        self.campoRacao.setGeometry(QtCore.QRect(400, 220, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoRacao.setFont(font)
        self.campoRacao.setStyleSheet("position: absolute;\n"
                                      "width: 692px;\n"
                                      "height: 51px;\n"
                                      "left: 625px;\n"
                                      "top: 264px;\n"
                                      "\n"
                                      "background: #D9D9D9;\n"
                                      "border-radius: 8px;")
        self.campoRacao.setObjectName("campoRacao")
        self.campoStatus = QtWidgets.QTextEdit(self.frame)
        self.campoStatus.setGeometry(QtCore.QRect(400, 170, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoStatus.setFont(font)
        self.campoStatus.setStyleSheet("position: absolute;\n"
                                       "width: 692px;\n"
                                       "height: 51px;\n"
                                       "left: 625px;\n"
                                       "top: 264px;\n"
                                       "\n"
                                       "background: #D9D9D9;\n"
                                       "border-radius: 8px;")
        self.campoStatus.setObjectName("campoStatus")
        self.campoBuscarCliente = QtWidgets.QTextEdit(self.frame)
        self.campoBuscarCliente.setGeometry(QtCore.QRect(180, 270, 370, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoBuscarCliente.setFont(font)
        self.campoBuscarCliente.setStyleSheet("position: absolute;\n"
                                              "width: 692px;\n"
                                              "height: 51px;\n"
                                              "left: 625px;\n"
                                              "top: 264px;\n"
                                              "\n"
                                              "background: #D9D9D9;\n"
                                              "border-radius: 8px;")
        self.campoBuscarCliente.setObjectName("campoBuscarCliente")
        self.campoTipo = QtWidgets.QTextEdit(self.frame)
        self.campoTipo.setGeometry(QtCore.QRect(380, 120, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoTipo.setFont(font)
        self.campoTipo.setStyleSheet("position: absolute;\n"
                                     "width: 692px;\n"
                                     "height: 51px;\n"
                                     "left: 625px;\n"
                                     "top: 264px;\n"
                                     "\n"
                                     "background: #D9D9D9;\n"
                                     "border-radius: 8px;")
        self.campoTipo.setObjectName("campoSexo")
        self.sexo = QtWidgets.QLabel(self.frame)
        self.sexo.setGeometry(QtCore.QRect(320, 130, 51, 21))
        self.sexo.setStyleSheet("position: absolute;\n"
                                "width: 184px;\n"
                                "height: 24px;\n"
                                "left: 420px;\n"
                                "top: 277px;\n"
                                "\n"
                                "font-family: \'Inter\';\n"
                                "font-style: normal;\n"
                                "font-weight: 300;\n"
                                "font-size: 20px;\n"
                                "line-height: 24px;\n"
                                "text-align: center;\n"
                                "\n"
                                "color: #000000;")
        self.sexo.setObjectName("sexo")
        self.idade = QtWidgets.QLabel(self.frame)
        self.idade.setGeometry(QtCore.QRect(30, 75, 61, 21))
        self.idade.setStyleSheet("position: absolute;\n"
                                 "width: 184px;\n"
                                 "height: 24px;\n"
                                 "left: 420px;\n"
                                 "top: 277px;\n"
                                 "\n"
                                 "font-family: \'Inter\';\n"
                                 "font-style: normal;\n"
                                 "font-weight: 300;\n"
                                 "font-size: 20px;\n"
                                 "line-height: 24px;\n"
                                 "text-align: center;\n"
                                 "\n"
                                 "color: #000000;")
        self.idade.setObjectName("idade")
        self.peso = QtWidgets.QLabel(self.frame)
        self.peso.setGeometry(QtCore.QRect(200, 75, 51, 20))
        self.peso.setStyleSheet("position: absolute;\n"
                                "width: 184px;\n"
                                "height: 24px;\n"
                                "left: 420px;\n"
                                "top: 277px;\n"
                                "\n"
                                "font-family: \'Inter\';\n"
                                "font-style: normal;\n"
                                "font-weight: 300;\n"
                                "font-size: 20px;\n"
                                "line-height: 24px;\n"
                                "text-align: center;\n"
                                "\n"
                                "color: #000000;")
        self.peso.setObjectName("peso")
        self.idadeBox = QtWidgets.QSpinBox(self.frame)
        self.idadeBox.setGeometry(QtCore.QRect(100, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.idadeBox.setFont(font)
        self.idadeBox.setObjectName("idadeBox")
        self.PesoBox = QtWidgets.QSpinBox(self.frame)
        self.PesoBox.setGeometry(QtCore.QRect(260, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PesoBox.setFont(font)
        self.PesoBox.setObjectName("PesoBox")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(460, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.btnSalvar = QtWidgets.QPushButton(self.container)
        self.btnSalvar.setGeometry(QtCore.QRect(20, 470, 141, 61))
        self.btnSalvar.setStyleSheet("position: absolute;\n"
                                     "width: 251px;\n"
                                     "height: 66px;\n"
                                     "left: 381px;\n"
                                     "top: 884px;\n"
                                     "\n"
                                     "background-color: rgb(85, 170, 127);\n"
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
        self.btnSalvar.setObjectName("btnSalvar")
        self.btnListar = QtWidgets.QPushButton(self.container)
        self.btnListar.setGeometry(QtCore.QRect(500, 470, 141, 61))
        self.btnListar.setStyleSheet("position: absolute;\n"
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
        self.btnListar.setObjectName("btnAtualizar")
        self.btnBusca = QtWidgets.QPushButton(self.container)
        self.btnBusca.setGeometry(QtCore.QRect(580, 330, 40, 40))
        self.btnBusca.setStyleSheet("position: absolute;\n"
                                    "width: 251px;\n"
                                    "height: 66px;\n"
                                    "left: 381px;\n"
                                    "top: 884px;\n"
                                    "\n"
                                    "background-color: rgb(85, 170, 127);\n"
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
        self.btnBusca.setObjectName("btnBusca")

        self.retranslateUi(Cadastrar)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar)
        idade = self.idadeBox.value()
        peso = self.PesoBox.value()

        self.btnSalvar.clicked.connect(self.insert)
        self.btnListar.clicked.connect(self.Listar_Animais)
        self.btnBusca.clicked.connect(self.selecionarCliente)

    def selecionarCliente(self):
        self.janela_listar_cliente = QtWidgets.QMainWindow()
        self.listar_cliente = ListaClienteAnimal()
        self.listar_cliente.setupUi(self.janela_listar_cliente)
        self.janela_listar_cliente.show()

    def insert(self):
        idcliente = self.listar_cliente.SelecionarCliente()
        idCli = 2
        print(idCli)
        nomeAnimal = self.campoNomeAnimal.toPlainText()
        idade = self.idadeBox.value()
        peso = self.PesoBox.value()
        sexo = self.comboBox.currentText()
        raca = self.campoRaca.toPlainText()
        tipo = self.campoTipo.toPlainText()
        porte = self.campoPorte.toPlainText()
        status = self.campoStatus.toPlainText()
        racao = self.campoRacao.toPlainText()
        tutor = self.campoBuscarCliente.toPlainText()

        animal = Animal(idCli, nomeAnimal, tipo, sexo, raca, peso,
                        idade, idcliente)
        AnimalController.controllerAnimal(animal)

        msg = QMessageBox()
        # msg.setIcon(QMessageBox.information)
        msg.setText("Animal Adicionado")
        msg.setWindowTitle("Adicionar Animal")
        # msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    def Listar_Cliente(self):
        self.janela_listar_cliente = QtWidgets.QMainWindow()
        self.clienteJanela = ListarCliente()
        self.clienteJanela.setupUi(self.janela_listar_cliente)
        self.janela_listar_cliente.show()

    def Listar_Animais(self):
        self.janela_listar_animais = QtWidgets.QMainWindow()
        self.animaisJanela = ListarAnimais()
        self.animaisJanela.setupUi(self.janela_listar_animais)
        self.janela_listar_animais.show()

    def retranslateUi(self, Cadastrar):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar.setWindowTitle(_translate("Cadastrar", "Cadastrar"))
        self.healthypets.setText(_translate("Cadastrar", "HEALTHY PETS"))
        self.txtCadastrar.setText(_translate("Cadastrar", "Cadastrar Animal"))
        self.nomeAnimal.setText(_translate("Cadastrar", "NOME DO ANIMAL"))
        self.porte.setText(_translate("Cadastrar", "PORTE"))
        self.raca.setText(_translate("Cadastrar", "RA??A"))
        self.racao.setText(_translate("Cadastrar", "RA????O"))
        self.status.setText(_translate("Cadastrar", "STATUS"))
        self.tutor.setText(_translate("Cadastrar", "BUSCAR TUTOR"))
        self.tipo.setText(_translate("Cadastrar", "SEXO"))
        self.sexo.setText(_translate("Cadastrar", "TIPO"))
        self.idade.setText(_translate("Cadastrar", "IDADE"))
        self.peso.setText(_translate("Cadastrar", "PESO"))
        self.comboBox.setItemText(0, _translate("Cadastrar", "MACHO"))
        self.comboBox.setItemText(1, _translate("Cadastrar", "FEMEA"))
        self.btnSalvar.setText(_translate("Cadastrar", "SALVAR"))
        self.btnListar.setText(_translate("Cadastrar", "LISTAR"))
        self.btnBusca.setText(_translate("Cadastrar", "B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastrar = QtWidgets.QWidget()
    ui = Ui_CadastrarAnimal()
    ui.setupUi(Cadastrar)
    Cadastrar.show()
    sys.exit(app.exec_())
