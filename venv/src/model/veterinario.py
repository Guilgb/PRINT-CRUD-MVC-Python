class Veterinario:
    def __init__(self, idVeterinario: int, nome: str, cpf: str, nascimento: str,
                 telefone: str, email: str, formacao: str):
        self.__idVeterinario = idVeterinario
        self.__nome = nome
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__telefone = telefone
        self.__email = email
        self.__formacao = formacao

    @property
    def idVeterinario(self):
        return self.__idVeterinario

    @idVeterinario.setter
    def idVeterinario(self, idVeterinario):
        self.__idVeterinario = idVeterinario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def nascimento(self):
        return self.__nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        self.__nascimento = nascimento

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def formacao(self):
        return self.__formacao

    @formacao.setter
    def formacao(self, formacao):
        self.__formacao = formacao

    def __str__(self) -> str:
        return (self.idVeterinario, self.nome, self.cpf, self.nascimento, self.telefone, self.email, self.formacao)
