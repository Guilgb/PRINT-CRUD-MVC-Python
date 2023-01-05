class Prontuario:
    def __init__(self, id: int, sexo: str, porte: str, especie: str,
                 dataProntuario: str, racaProntuario: str):
        self.__id = id
        self.__sexo = sexo
        self.__porte = porte
        self.__especie = especie
        self.__dataProntuario = dataProntuario
        self.__racaProntuario = racaProntuario

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def porte(self):
        return self.__porte

    @id.setter
    def porte(self, porte):
        self.__porte = porte

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, especie):
        self.__especie = especie

    @property
    def dataProntuario(self):
        return self.__dataProntuario

    @dataProntuario.setter
    def dataProntuario(self, dataProntuario):
        self.__dataProntuario = dataProntuario

    @property
    def racaProntuario(self):
        return self.__racaProntuario

    @racaProntuario.setter
    def racaProntuario(self, racaProntuario):
        self.__racaProntuario = racaProntuario

    def __str__(self) -> str:
        return self.porte
