# Form implementation generated from reading ui file 'c:\Users\guilh\Documents\PRINT\design\AgendarConsulta.ui'
#
# Created by: PyQt6 UI code generator 6.4.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Cadastrar(object):
    def setupUi(self, Cadastrar):
        Cadastrar.setObjectName("Cadastrar")
        Cadastrar.resize(900, 600)
        Cadastrar.setMinimumSize(QtCore.QSize(900, 240))
        Cadastrar.setMaximumSize(QtCore.QSize(900, 600))
        self.navegation = QtWidgets.QFrame(parent=Cadastrar)
        self.navegation.setGeometry(QtCore.QRect(0, 0, 221, 741))
        self.navegation.setStyleSheet("background-color: rgb(48, 68, 86)")
        self.navegation.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.navegation.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.navegation.setObjectName("navegation")
        self.btnInicio = QtWidgets.QPushButton(parent=self.navegation)
        self.btnInicio.setGeometry(QtCore.QRect(0, 110, 221, 101))
        self.btnInicio.setAutoFillBackground(False)
        self.btnInicio.setStyleSheet("background-color: rgb(48, 68, 86);\n"
"color: white;")
        self.btnInicio.setObjectName("btnInicio")
        self.btnCadastrar = QtWidgets.QPushButton(parent=self.navegation)
        self.btnCadastrar.setGeometry(QtCore.QRect(0, 210, 221, 101))
        self.btnCadastrar.setAutoFillBackground(False)
        self.btnCadastrar.setStyleSheet("background-color: rgb(91, 113, 133);\n"
"color: white;")
        self.btnCadastrar.setObjectName("btnCadastrar")
        self.healthypets = QtWidgets.QPushButton(parent=self.navegation)
        self.healthypets.setEnabled(False)
        self.healthypets.setGeometry(QtCore.QRect(0, 0, 221, 111))
        self.healthypets.setAccessibleName("")
        self.healthypets.setAutoFillBackground(False)
        self.healthypets.setStyleSheet("background-color: rgb(91, 113, 133);\n"
"color: white;")
        self.healthypets.setObjectName("healthypets")
        self.btnAgendar = QtWidgets.QPushButton(parent=self.navegation)
        self.btnAgendar.setGeometry(QtCore.QRect(0, 310, 221, 101))
        self.btnAgendar.setAutoFillBackground(False)
        self.btnAgendar.setStyleSheet("background-color: rgb(48, 68, 86);\n"
"color: white;")
        self.btnAgendar.setObjectName("btnAgendar")
        self.btnProntuario = QtWidgets.QPushButton(parent=self.navegation)
        self.btnProntuario.setGeometry(QtCore.QRect(0, 410, 221, 101))
        self.btnProntuario.setAutoFillBackground(False)
        self.btnProntuario.setStyleSheet("background-color: rgb(91, 113, 133);\n"
"color: white;")
        self.btnProntuario.setObjectName("btnProntuario")
        self.container = QtWidgets.QFrame(parent=Cadastrar)
        self.container.setGeometry(QtCore.QRect(220, 0, 920, 600))
        self.container.setMinimumSize(QtCore.QSize(920, 600))
        self.container.setMaximumSize(QtCore.QSize(920, 740))
        self.container.setStyleSheet("background-color:rgb(201, 201, 201)")
        self.container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.container.setObjectName("container")
        self.txtCadastrar = QtWidgets.QLabel(parent=self.container)
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
        self.frame = QtWidgets.QFrame(parent=self.container)
        self.frame.setGeometry(QtCore.QRect(20, 60, 621, 321))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.buscaAnimal = QtWidgets.QLabel(parent=self.frame)
        self.buscaAnimal.setGeometry(QtCore.QRect(10, 30, 171, 21))
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
        self.data = QtWidgets.QLabel(parent=self.frame)
        self.data.setGeometry(QtCore.QRect(10, 210, 51, 20))
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
        self.hora = QtWidgets.QLabel(parent=self.frame)
        self.hora.setGeometry(QtCore.QRect(220, 210, 81, 20))
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
        self.retorno = QtWidgets.QLabel(parent=self.frame)
        self.retorno.setGeometry(QtCore.QRect(10, 270, 121, 20))
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
        self.buscaCliente = QtWidgets.QLabel(parent=self.frame)
        self.buscaCliente.setGeometry(QtCore.QRect(10, 90, 161, 21))
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
        self.campoBuscarAnimal = QtWidgets.QTextEdit(parent=self.frame)
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
        self.campoBuscarCliente = QtWidgets.QTextEdit(parent=self.frame)
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
        self.campoData = QtWidgets.QTextEdit(parent=self.frame)
        self.campoData.setGeometry(QtCore.QRect(80, 200, 111, 41))
        self.campoData.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoData.setObjectName("campoData")
        self.campoHora = QtWidgets.QTextEdit(parent=self.frame)
        self.campoHora.setGeometry(QtCore.QRect(280, 200, 101, 41))
        self.campoHora.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoHora.setObjectName("campoHora")
        self.campoRetorno = QtWidgets.QTextEdit(parent=self.frame)
        self.campoRetorno.setGeometry(QtCore.QRect(140, 260, 421, 41))
        self.campoRetorno.setStyleSheet("position: absolute;\n"
"width: 692px;\n"
"height: 51px;\n"
"left: 625px;\n"
"top: 264px;\n"
"\n"
"background: #D9D9D9;\n"
"border-radius: 8px;")
        self.campoRetorno.setObjectName("campoRetorno")
        self.campoBuscarVeterinario = QtWidgets.QTextEdit(parent=self.frame)
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
        self.buscaVeterinario = QtWidgets.QLabel(parent=self.frame)
        self.buscaVeterinario.setGeometry(QtCore.QRect(10, 150, 201, 21))
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
        self.btnSalvar = QtWidgets.QPushButton(parent=self.container)
        self.btnSalvar.setGeometry(QtCore.QRect(20, 390, 141, 61))
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
        self.btnAtualizar = QtWidgets.QPushButton(parent=self.container)
        self.btnAtualizar.setGeometry(QtCore.QRect(500, 400, 141, 61))
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

    def retranslateUi(self, Cadastrar):
        _translate = QtCore.QCoreApplication.translate
        Cadastrar.setWindowTitle(_translate("Cadastrar", "Cadastrar"))
        self.btnInicio.setText(_translate("Cadastrar", "INICIO"))
        self.btnCadastrar.setText(_translate("Cadastrar", "CADASTRAR"))
        self.healthypets.setText(_translate("Cadastrar", "HEALTHY PETS"))
        self.btnAgendar.setText(_translate("Cadastrar", "AGENDAR"))
        self.btnProntuario.setText(_translate("Cadastrar", "PRONTUÁRIO"))
        self.txtCadastrar.setText(_translate("Cadastrar", "Agendar Consulta"))
        self.buscaAnimal.setText(_translate("Cadastrar", "BUSCAR ANIMAL"))
        self.data.setText(_translate("Cadastrar", "DATA"))
        self.hora.setText(_translate("Cadastrar", "HORA"))
        self.retorno.setText(_translate("Cadastrar", "OBSERVAÇÃO"))
        self.buscaCliente.setText(_translate("Cadastrar", "BUSCAR CLIENTE"))
        self.buscaVeterinario.setText(_translate("Cadastrar", "BUSCAR VETERINÁRIO"))
        self.btnSalvar.setText(_translate("Cadastrar", "SALVAR"))
        self.btnAtualizar.setText(_translate("Cadastrar", "BUSCAR"))
