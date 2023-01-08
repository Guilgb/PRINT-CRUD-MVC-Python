from src.model.animal import Animal
from src.model.vacina import Vacina
from src.model.veterinario import Veterinario


class Prontuario:
    def __init__(self, idProntuario: int, sexo: str, porte: str, especie: str,
                 dataProntuario: str, racaProntuario: str, animal: Animal,
                 veterinario: Veterinario, vacina: Vacina):

        self.__idProntuario = idProntuario
        self.__sexo = sexo
        self.__porte = porte
        self.__especie = especie
        self.__dataProntuario = dataProntuario
        self.__racaProntuario = racaProntuario
        self.__animal = animal
        self.__veterinario = veterinario
        self.__vacina = vacina

    @property
    def idProntuario(self):
        return self.__idProntuario

    @idProntuario.setter
    def idProntuario(self, idProntuario):
        self.__idProntuario = idProntuario

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def porte(self):
        return self.__porte

    @porte.setter
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

    @property
    def animal(self):
        return self.__animal

    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def veterinario(self):
        return self.__veterinario

    @veterinario.setter
    def veterinario(self, veterinario):
        self.__veterinario = veterinario

    @property
    def vacina(self):
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        self.__vacina = vacina

    def __str__(self) -> str:
        return self.especie
