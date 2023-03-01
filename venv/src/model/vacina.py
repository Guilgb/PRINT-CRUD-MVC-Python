class Vacina:
    def __init__(self, idVacina: int, nomeVacina: str, fabricante: str, 
                 validade: str, volume: str):
        self.__idVacina = idVacina
        self.__nomeVacina = nomeVacina
        self.__fabricante = fabricante
        self.__validade = validade
        self.__volume = volume

    @property
    def idVacina(self):
        return self.__idVacina

    @idVacina.setter
    def idVacina(self, idVacina):
        self.__idVacina = idVacina

    @property
    def nomeVacina(self):
        return self.__nomeVacina

    @nomeVacina.setter
    def nomeVacina(self, nomeVacina):
        self.__id = nomeVacina

    @property
    def fabricante(self):
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante

    @property
    def validade(self):
        return self.__validade

    @validade.setter
    def validade(self, validade):
        self.__validade = validade

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, volume):
        self.__volume = volume
