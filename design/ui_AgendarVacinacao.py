# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\guilh\Documents\PRINT\design\AgendarVacinacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadastrarVacina(object):
    def setupUi(self, CadastrarVacina):
        CadastrarVacina.setObjectName("CadastrarVacina")
        CadastrarVacina.resize(900, 600)
        CadastrarVacina.setMinimumSize(QtCore.QSize(900, 240))
        CadastrarVacina.setMaximumSize(QtCore.QSize(900, 600))
        self.navegation = QtWidgets.QFrame(CadastrarVacina)
        self.navegation.setGeometry(QtCore.QRect(0, 0, 221, 741))
        self.navegation.setStyleSheet("background-color: rgb(48, 68, 86)")
        self.navegation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.navegation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.navegation.setObjectName("navegation")
        self.btnInicio = QtWidgets.QPushButton(self.navegation)
        self.btnInicio.setGeometry(QtCore.QRect(0, 110, 221, 101))
        self.btnInicio.setAutoFillBackground(False)
        self.btnInicio.setStyleSheet("background-color: rgb(48, 68, 86);\n"
"color: white;")
        self.btnInicio.setObjectName("btnInicio")
        self.btnCadastrar = QtWidgets.QPushButton(self.navegation)
        self.btnCadastrar.setGeometry(QtCore.QRect(0, 210, 221, 101))
        self.btnCadastrar.setAutoFillBackground(False)
        self.btnCadastrar.setStyleSheet("background-color: rgb(91, 113, 133);\n"
"color: white;")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.healthypets = QtWidgets.QPushButton(self.navegation)
        self.healthypets.setEnabled(False)
        self.healthypets.setGeometry(QtCore.QRect(0, 0, 221, 111))
        self.healthypets.setAccessibleName("")
        self.healthypets.setAutoFillBackground(False)
        self.healthypets.setStyleSheet("background-color: rgb(91, 113, 133);\n"
"color: white;")
        self.healthypets.setObjectName("healthypets")
        self.btnAgendar = QtWidgets.QPushButton(self.navegation)
        self.btnAgendar.setGeometry(QtCore.QRect(0, 310, 221, 101))
        self.btnAgendar.setAutoFillBackground(False)
        self.btnAgendar.setStyleSheet("background-color: rgb(48, 68, 86);\n"
"color: white;")
        self.btnAgendar.setObjectName("btnAgendar")
        self.btnProntuario = QtWidgets.QPushButton(self.navegation)
        self.btnProntuario.setGeometry(QtCore.QRect(0, 410, 221, 101))
        self.btnProntuario.setAutoFillBackground(False)
        self.btnProntuario.setStyleSheet("background-color: rgb(91, 113, 133);\n"
"color: white;")
        self.btnProntuario.setObjectName("btnProntuario")
        self.container = QtWidgets.QFrame(CadastrarVacina)
        self.container.setGeometry(QtCore.QRect(220, 0, 920, 600))
        self.container.setMinimumSize(QtCore.QSize(920, 600))
        self.container.setMaximumSize(QtCore.QSize(920, 740))
        self.container.setStyleSheet("background-color:rgb(201, 201, 201)")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.txtCadastrar = QtWidgets.QLabel(self.container)
        self.txtCadastrar.setGeometry(QtCore.QRect(30, 10, 311, 51))
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
        self.buscaAnimal = QtWidgets.QLabel(self.frame)
        self.buscaAnimal.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.buscaAnimal.setStyleSheet("position: absolute;\n"
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
        self.buscaAnimal.setObjectName("buscaAnimal")
        self.buscaVacina = QtWidgets.QLabel(self.frame)
        self.buscaVacina.setGeometry(QtCore.QRect(10, 210, 151, 16))
        self.buscaVacina.setStyleSheet("position: absolute;\n"
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
        self.buscaVacina.setObjectName("buscaVacina")
        self.data = QtWidgets.QLabel(self.frame)
        self.data.setGeometry(QtCore.QRect(10, 270, 51, 20))
        self.data.setStyleSheet("position: absolute;\n"
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
        self.data.setObjectName("data")
        self.hora = QtWidgets.QLabel(self.frame)
        self.hora.setGeometry(QtCore.QRect(200, 270, 51, 20))
        self.hora.setStyleSheet("position: absolute;\n"
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
        self.hora.setObjectName("hora")
        self.dataProxDose = QtWidgets.QLabel(self.frame)
        self.dataProxDose.setGeometry(QtCore.QRect(20, 330, 201, 16))
        self.dataProxDose.setStyleSheet("position: absolute;\n"
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
        self.dataProxDose.setObjectName("dataProxDose")
        self.buscaCliente = QtWidgets.QLabel(self.frame)
        self.buscaCliente.setGeometry(QtCore.QRect(10, 90, 151, 21))
        self.buscaCliente.setStyleSheet("position: absolute;\n"
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
        self.buscaCliente.setObjectName("buscaCliente")
        self.campoBuscarAnimal = QtWidgets.QTextEdit(self.frame)
        self.campoBuscarAnimal.setGeometry(QtCore.QRect(170, 20, 431, 41))
        self.campoBuscarAnimal.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoBuscarAnimal.setObjectName("campoBuscarAnimal")
        self.campoBuscarCliente = QtWidgets.QTextEdit(self.frame)
        self.campoBuscarCliente.setGeometry(QtCore.QRect(170, 80, 431, 41))
        self.campoBuscarCliente.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoBuscarCliente.setObjectName("campoBuscarCliente")
        self.campoBuscarVacina = QtWidgets.QTextEdit(self.frame)
        self.campoBuscarVacina.setGeometry(QtCore.QRect(180, 200, 421, 41))
        self.campoBuscarVacina.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoBuscarVacina.setObjectName("campoBuscarVacina")
        self.campoData = QtWidgets.QTextEdit(self.frame)
        self.campoData.setGeometry(QtCore.QRect(80, 260, 111, 41))
        self.campoData.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoData.setObjectName("campoData")
        self.campoHora = QtWidgets.QTextEdit(self.frame)
        self.campoHora.setGeometry(QtCore.QRect(260, 260, 101, 41))
        self.campoHora.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoHora.setObjectName("campoHora")
        self.campoProxDose = QtWidgets.QTextEdit(self.frame)
        self.campoProxDose.setGeometry(QtCore.QRect(230, 320, 251, 41))
        self.campoProxDose.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoProxDose.setObjectName("campoProxDose")
        self.campoBuscarVeterinario = QtWidgets.QTextEdit(self.frame)
        self.campoBuscarVeterinario.setGeometry(QtCore.QRect(220, 140, 381, 41))
        self.campoBuscarVeterinario.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoBuscarVeterinario.setObjectName("campoBuscarVeterinario")
        self.buscaVeterinario = QtWidgets.QLabel(self.frame)
        self.buscaVeterinario.setGeometry(QtCore.QRect(10, 150, 201, 16))
        self.buscaVeterinario.setStyleSheet("position: absolute;\n"
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
        self.buscaVeterinario.setObjectName("buscaVeterinario")
        self.fase = QtWidgets.QLabel(self.frame)
        self.fase.setGeometry(QtCore.QRect(370, 271, 51, 20))
        self.fase.setStyleSheet("position: absolute;\n"
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
        self.fase.setObjectName("fase")
        self.campoFase = QtWidgets.QTextEdit(self.frame)
        self.campoFase.setGeometry(QtCore.QRect(430, 260, 171, 41))
        self.campoFase.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoFase.setObjectName("campoFase")
        self.btnSalvar = QtWidgets.QPushButton(self.container)
        self.btnSalvar.setGeometry(QtCore.QRect(490, 490, 141, 61))
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
        self.btnListar.setGeometry(QtCore.QRect(20, 490, 141, 61))
        self.btnListar.setStyleSheet("position: absolute;\n"
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
        self.btnListar.setObjectName("btnListar")

        self.retranslateUi(CadastrarVacina)
        QtCore.QMetaObject.connectSlotsByName(CadastrarVacina)

    def retranslateUi(self, CadastrarVacina):
        _translate = QtCore.QCoreApplication.translate
        CadastrarVacina.setWindowTitle(_translate("CadastrarVacina", "Cadastrar"))
        self.btnInicio.setText(_translate("CadastrarVacina", "INICIO"))
        self.btnCadastrar.setText(_translate("CadastrarVacina", "CADASTRAR"))
        self.healthypets.setText(_translate("CadastrarVacina", "HEALTHY PETS"))
        self.btnAgendar.setText(_translate("CadastrarVacina", "AGENDAR"))
        self.btnProntuario.setText(_translate("CadastrarVacina", "PRONTUÁRIO"))
        self.txtCadastrar.setText(_translate("CadastrarVacina", "Agendar Vacinação"))
        self.buscaAnimal.setText(_translate("CadastrarVacina", "BUSCAR ANIMAL"))
        self.buscaVacina.setText(_translate("CadastrarVacina", "BUSCAR VACINA"))
        self.data.setText(_translate("CadastrarVacina", "DATA"))
        self.hora.setText(_translate("CadastrarVacina", "HORA"))
        self.dataProxDose.setText(_translate("CadastrarVacina", "DATA PRÓXIMA DOSE"))
        self.buscaCliente.setText(_translate("CadastrarVacina", "BUSCAR CLIENTE"))
        self.buscaVeterinario.setText(_translate("CadastrarVacina", "BUSCAR VETERINÁRIO"))
        self.fase.setText(_translate("CadastrarVacina", "FASE"))
        self.btnSalvar.setText(_translate("CadastrarVacina", "SALVAR"))
        self.btnListar.setText(_translate("CadastrarVacina", "LISTAR"))
