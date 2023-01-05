class Animal():
    def __init__(self, id: int, nomeAnimal: str, especie: str, sexo: str,
                 raca: str, peso: float, nascimento: str):
        self.__id = id
        self.__nomeAnimal = nomeAnimal
        self.__especie = especie
        self.__sexo = sexo
        self.__raca = raca
        self.__peso = peso
        self.__nascimento = nascimento

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nomeAnimal(self):
        return self.__nomeAnimal

    @nomeAnimal.setter
    def nomeAnimal(self, nomeAnimal):
        self.__nomeAnimal = nomeAnimal

    @property
    def especie(self):
        return self.__especie

    @especie.setter
    def especie(self, especie):
        self.__especie = especie

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, peso):
        self.__peso = peso

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    def __str__(self) -> str:
        return self.__nomeAnimal
