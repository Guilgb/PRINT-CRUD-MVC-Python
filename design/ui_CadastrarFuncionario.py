# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\guilh\Documents\PRINT\design\CadastrarFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CadastrarCliente(object):
    def setupUi(self, CadastrarCliente):
        CadastrarCliente.setObjectName("CadastrarCliente")
        CadastrarCliente.resize(900, 566)
        CadastrarCliente.setMinimumSize(QtCore.QSize(900, 240))
        CadastrarCliente.setMaximumSize(QtCore.QSize(900, 600))
        self.navegation = QtWidgets.QFrame(CadastrarCliente)
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
        self.healthypets = QtWidgets.QPushButton(self.navegation)
        self.healthypets.setEnabled(False)
        self.healthypets.setGeometry(QtCore.QRect(0, 0, 221, 111))
        self.healthypets.setAccessibleName("")
        self.healthypets.setAutoFillBackground(False)
        self.healthypets.setStyleSheet("background-color: rgb(91, 113, 133);\n"
"color: white;")
        self.healthypets.setObjectName("healthypets")
        self.container = QtWidgets.QFrame(CadastrarCliente)
        self.container.setGeometry(QtCore.QRect(220, 0, 920, 600))
        self.container.setMinimumSize(QtCore.QSize(920, 600))
        self.container.setMaximumSize(QtCore.QSize(920, 740))
        self.container.setStyleSheet("background-color:rgb(201, 201, 201)")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.txtCadastrar = QtWidgets.QLabel(self.container)
        self.txtCadastrar.setGeometry(QtCore.QRect(30, 10, 361, 51))
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
        self.frame.setGeometry(QtCore.QRect(30, 70, 621, 331))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nome = QtWidgets.QLabel(self.frame)
        self.nome.setGeometry(QtCore.QRect(20, 30, 221, 21))
        self.nome.setStyleSheet("position: absolute;\n"
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
        self.nome.setObjectName("nome")
        self.nascimento = QtWidgets.QLabel(self.frame)
        self.nascimento.setGeometry(QtCore.QRect(20, 90, 211, 21))
        self.nascimento.setStyleSheet("position: absolute;\n"
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
        self.nascimento.setObjectName("nascimento")
        self.telefone = QtWidgets.QLabel(self.frame)
        self.telefone.setGeometry(QtCore.QRect(20, 210, 71, 21))
        self.telefone.setStyleSheet("position: absolute;\n"
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
        self.telefone.setObjectName("telefone")
        self.email = QtWidgets.QLabel(self.frame)
        self.email.setGeometry(QtCore.QRect(20, 150, 61, 21))
        self.email.setStyleSheet("position: absolute;\n"
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
        self.email.setObjectName("email")
        self.campoNome = QtWidgets.QTextEdit(self.frame)
        self.campoNome.setGeometry(QtCore.QRect(250, 20, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoNome.setFont(font)
        self.campoNome.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoNome.setObjectName("campoNome")
        self.campoEmail = QtWidgets.QTextEdit(self.frame)
        self.campoEmail.setGeometry(QtCore.QRect(90, 140, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoEmail.setFont(font)
        self.campoEmail.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoEmail.setObjectName("campoEmail")
        self.campoCargo = QtWidgets.QTextEdit(self.frame)
        self.campoCargo.setGeometry(QtCore.QRect(90, 200, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoCargo.setFont(font)
        self.campoCargo.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoCargo.setObjectName("campoCargo")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(240, 80, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dateEdit.setFont(font)
        self.dateEdit.setMouseTracking(False)
        self.dateEdit.setObjectName("dateEdit")
        self.campoTelefone = QtWidgets.QTextEdit(self.frame)
        self.campoTelefone.setGeometry(QtCore.QRect(90, 260, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoTelefone.setFont(font)
        self.campoTelefone.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoTelefone.setObjectName("campoTelefone")
        self.telefone_2 = QtWidgets.QLabel(self.frame)
        self.telefone_2.setGeometry(QtCore.QRect(20, 270, 71, 21))
        self.telefone_2.setStyleSheet("position: absolute;\n"
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
        self.telefone_2.setObjectName("telefone_2")
        self.btnSalvar = QtWidgets.QPushButton(self.container)
        self.btnSalvar.setGeometry(QtCore.QRect(30, 410, 141, 61))
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
        self.btnAtualizar = QtWidgets.QPushButton(self.container)
        self.btnAtualizar.setGeometry(QtCore.QRect(510, 410, 141, 61))
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

        self.retranslateUi(CadastrarCliente)
        QtCore.QMetaObject.connectSlotsByName(CadastrarCliente)

    def retranslateUi(self, CadastrarCliente):
        _translate = QtCore.QCoreApplication.translate
        CadastrarCliente.setWindowTitle(_translate("CadastrarCliente", "Cadastrar"))
        self.btnInicio.setText(_translate("CadastrarCliente", "INICIO"))
        self.healthypets.setText(_translate("CadastrarCliente", "HEALTHY PETS"))
        self.txtCadastrar.setText(_translate("CadastrarCliente", "Cadastrar Funcionario"))
        self.nome.setText(_translate("CadastrarCliente", "NOME DO FUNCIONARIO"))
        self.nascimento.setText(_translate("CadastrarCliente", "DATA DE NASCIMENTO"))
        self.telefone.setText(_translate("CadastrarCliente", "CARGO"))
        self.email.setText(_translate("CadastrarCliente", "E-MAIL"))
        self.telefone_2.setText(_translate("CadastrarCliente", "CARGO"))
        self.btnSalvar.setText(_translate("CadastrarCliente", "SALVAR"))
        self.btnAtualizar.setText(_translate("CadastrarCliente", "LISTAR"))
