class Veterinario:
    def __init__(self, idVeterinario: int, nomeVeterinario: str, cpfVeterinario: str, nascimentoVeterinario: str,
                 telefoneVeterinario: str, emailVeterinario: str,
                 formacao: str):
        self.__idVeterinario = idVeterinario
        self.__nomeVeterinario = nomeVeterinario
        self.__cpfVeterinario = cpfVeterinario
        self.__nascimentoVeterinario = nascimentoVeterinario
        self.__telefoneVeterinario = telefoneVeterinario
        self.__emailVeterinario = emailVeterinario
        self.__formacao = formacao

    @property
    def idVeterinario(self):
        return self.__idVeterinario

    @idVeterinario.setter
    def idVeterinario(self, idVeterinario):
        self.__idVeterinario = idVeterinario

    @property
    def nomeVeterinario(self):
        return self.__nomeVeterinario

    @nomeVeterinario.setter
    def nomeVeterinario(self, nomeVeterinario):
        self.__nomeVeterinario = nomeVeterinario

    @property
    def cpfVeterinario(self):
        return self.__cpfVeterinario

    @cpfVeterinario.setter
    def cpfVeterinario(self, cpfVeterinario):
        self.__cpfVeterinario = cpfVeterinario

    @property
    def nascimentoVeterinario(self):
        return self.__nascimentoVeterinario

    @nascimentoVeterinario.setter
    def nascimentoVeterinario(self, nascimentoVeterinario):
        self.__nascimentoVeterinario = nascimentoVeterinario

    @property
    def telefoneVeterinario(self):
        return self.__telefoneVeterinario

    @telefoneVeterinario.setter
    def telefoneVeterinario(self, telefoneVeterinario):
        self.__telefoneVeterinario = telefoneVeterinario

    @property
    def emailVeterinario(self):
        return self.__emailVeterinario

    @emailVeterinario.setter
    def emailVeterinario(self, emailVeterinario):
        self.__emailVeterinario = emailVeterinario

    @property
    def formacao(self):
        return self.__formacao

    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao

    def __str__(self) -> str:
        return (self.idVeterinario, self.nomeVeterinario, self.cpfVeterinario,
                self.nascimentoVeterinario, self.telefoneVeterinario,
                self.emailVeterinario, self.formacao)
