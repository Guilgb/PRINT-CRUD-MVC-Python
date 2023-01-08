class Funcionario:
    def __init__(self, idFuncionario: int, nomeFuncionario: str, nascimentoFuncionario: str, emailFuncionario: str, telefoneFuncionario: str, cargo: str):
        self.__idFuncionario = idFuncionario
        self.__nomeFuncionario = nomeFuncionario
        self.__nascimentoFuncionario = nascimentoFuncionario
        self.__emailFuncionario = emailFuncionario
        self.__telefoneFuncionario = telefoneFuncionario
        self.__cargo = cargo

    @property
    def idFuncionario(self):
        return self.__idFuncionario

    @idFuncionario.setter
    def idFuncionario(self, idFuncionario):
        self.__idFuncionario = idFuncionario

    @property
    def nomeFuncionario(self):
        return self.__nomeFuncionario

    @nomeFuncionario.setter
    def nomeFuncionario(self, nomeFuncionario):
        self.__nomeFuncionario = nomeFuncionario

    @property
    def nascimentoFuncionario(self):
        return self.__nascimentoFuncionario

    @nascimentoFuncionario.setter
    def nascimentoFuncionario(self, nascimentoFuncionario):
        self.__nascimentoFuncionario = nascimentoFuncionario

    @property
    def emailFuncionario(self):
        return self.__emailFuncionario

    @emailFuncionario.setter
    def emailFuncionario(self, emailFuncionario):
        self.__emailFuncionario = emailFuncionario

    @property
    def telefoneFuncionario(self):
        return self.__telefoneFuncionario

    @telefoneFuncionario.setter
    def telefoneFuncionario(self, telefoneFuncionario):
        self.__telefoneFuncionario = telefoneFuncionario

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__idFuncionario = cargo





