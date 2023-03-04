# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\guilh\Documents\PRINT\design\ListagemVeterinario.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cadastrar(object):
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
        self.container = QtWidgets.QFrame(Cadastrar)
        self.container.setGeometry(QtCore.QRect(220, 0, 920, 600))
        self.container.setMinimumSize(QtCore.QSize(920, 600))
        self.container.setMaximumSize(QtCore.QSize(920, 740))
        self.container.setStyleSheet("background-color:rgb(201, 201, 201)")
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.txtCadastrar = QtWidgets.QLabel(self.container)
        self.txtCadastrar.setGeometry(QtCore.QRect(30, 10, 431, 51))
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
        self.listagemCliente = QtWidgets.QTableWidget(self.frame)
        self.listagemCliente.setGeometry(QtCore.QRect(20, 10, 591, 431))
        self.listagemCliente.setStyleSheet("position: absolute;\n"
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
        self.listagemCliente.setObjectName("listagemCliente")
        self.listagemCliente.setColumnCount(7)
        self.listagemCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listagemCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.listagemCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemCliente.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.listagemCliente.setHorizontalHeaderItem(6, item)
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

        self.retranslateUi(Cadastrar)
        QtCore.QMetaObject.connectSlotsByName(Cadastrar)

    def retranslateUi(self, Cadastrar):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar.setWindowTitle(_translate("Cadastrar", "Cadastrar"))
        self.btnInicio.setText(_translate("Cadastrar", "INICIO"))
        self.healthypets.setText(_translate("Cadastrar", "HEALTHY PETS"))
        self.txtCadastrar.setText(_translate("Cadastrar", "LISTAGEM VATERINÁRIO"))
        item = self.listagemCliente.horizontalHeaderItem(0)
        item.setText(_translate("Cadastrar", "ID"))
        item = self.listagemCliente.horizontalHeaderItem(1)
        item.setText(_translate("Cadastrar", "NOME"))
        item = self.listagemCliente.horizontalHeaderItem(2)
        item.setText(_translate("Cadastrar", "NASCIMENTO"))
        item = self.listagemCliente.horizontalHeaderItem(3)
        item.setText(_translate("Cadastrar", "CPF"))
        item = self.listagemCliente.horizontalHeaderItem(4)
        item.setText(_translate("Cadastrar", "TELEFONE"))
        item = self.listagemCliente.horizontalHeaderItem(5)
        item.setText(_translate("Cadastrar", "EMAIL"))
        item = self.listagemCliente.horizontalHeaderItem(6)
        item.setText(_translate("Cadastrar", "FORMAÇÃO"))
        self.btnAtualizar.setText(_translate("Cadastrar", "ATUALIZAR"))
        self.btnRemover.setText(_translate("Cadastrar", "REMOVER"))
