# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\guilh\Documents\PRINT\design\AtualizarConsulta.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AgendarConsulta(object):
    def setupUi(self, AgendarConsulta):
        AgendarConsulta.setObjectName("AgendarConsulta")
        AgendarConsulta.resize(900, 600)
        AgendarConsulta.setMinimumSize(QtCore.QSize(900, 240))
        AgendarConsulta.setMaximumSize(QtCore.QSize(900, 600))
        self.navegation = QtWidgets.QFrame(AgendarConsulta)
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
        self.container = QtWidgets.QFrame(AgendarConsulta)
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
        self.frame.setGeometry(QtCore.QRect(20, 60, 621, 321))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.buscaAnimal = QtWidgets.QLabel(self.frame)
        self.buscaAnimal.setGeometry(QtCore.QRect(10, 30, 71, 21))
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
        self.data = QtWidgets.QLabel(self.frame)
        self.data.setGeometry(QtCore.QRect(10, 150, 51, 20))
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
        self.hora.setGeometry(QtCore.QRect(220, 150, 51, 20))
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
        self.retorno = QtWidgets.QLabel(self.frame)
        self.retorno.setGeometry(QtCore.QRect(10, 209, 131, 21))
        self.retorno.setStyleSheet("position: absolute;\n"
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
        self.retorno.setObjectName("retorno")
        self.buscaCliente = QtWidgets.QLabel(self.frame)
        self.buscaCliente.setGeometry(QtCore.QRect(10, 90, 131, 21))
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
        self.campoBuscarAnimal.setGeometry(QtCore.QRect(89, 20, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoBuscarAnimal.setFont(font)
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
        self.campoBuscarCliente.setGeometry(QtCore.QRect(149, 80, 401, 41))
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
        self.campoRetorno = QtWidgets.QTextEdit(self.frame)
        self.campoRetorno.setGeometry(QtCore.QRect(140, 200, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.campoRetorno.setFont(font)
        self.campoRetorno.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoRetorno.setObjectName("campoRetorno")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(70, 150, 110, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(290, 150, 118, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.timeEdit.setFont(font)
        self.timeEdit.setObjectName("timeEdit")
        self.buscasAnimal = QtWidgets.QPushButton(self.frame)
        self.buscasAnimal.setGeometry(QtCore.QRect(557, 20, 51, 41))
        self.buscasAnimal.setStyleSheet("position: absolute;\n"
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
        self.buscasAnimal.setObjectName("buscasAnimal")
        self.BuscarFuncionario = QtWidgets.QPushButton(self.frame)
        self.BuscarFuncionario.setGeometry(QtCore.QRect(558, 80, 51, 41))
        self.BuscarFuncionario.setStyleSheet("position: absolute;\n"
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
        self.BuscarFuncionario.setObjectName("BuscarFuncionario")
        self.btnAtualizar = QtWidgets.QPushButton(self.container)
        self.btnAtualizar.setGeometry(QtCore.QRect(20, 390, 141, 61))
        self.btnAtualizar.setStyleSheet("position: absolute;\n"
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
        self.btnAtualizar.setObjectName("btnAtualizar")

        self.retranslateUi(AgendarConsulta)
        QtCore.QMetaObject.connectSlotsByName(AgendarConsulta)

    def retranslateUi(self, AgendarConsulta):
        _translate = QtCore.QCoreApplication.translate
        AgendarConsulta.setWindowTitle(_translate("AgendarConsulta", "Cadastrar"))
        self.btnInicio.setText(_translate("AgendarConsulta", "INICIO"))
        self.healthypets.setText(_translate("AgendarConsulta", "HEALTHY PETS"))
        self.txtCadastrar.setText(_translate("AgendarConsulta", "Atualizar Consulta"))
        self.buscaAnimal.setText(_translate("AgendarConsulta", "ANIMAL"))
        self.data.setText(_translate("AgendarConsulta", "DATA"))
        self.hora.setText(_translate("AgendarConsulta", "HORA"))
        self.retorno.setText(_translate("AgendarConsulta", "OBSERVAÇÃO"))
        self.buscaCliente.setText(_translate("AgendarConsulta", "FUNCIONARIO"))
        self.buscasAnimal.setText(_translate("AgendarConsulta", "B"))
        self.BuscarFuncionario.setText(_translate("AgendarConsulta", "B"))
        self.btnAtualizar.setText(_translate("AgendarConsulta", "Atualizar"))