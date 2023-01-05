class Cliente:
    def __init__(self, id: int, nomeCliente: str, cpf: str, nascimento: str,
                 email: str, endereco: str, bairro: str, n_rua: int, telefone: str):
        self.__id = id
        self.__nomeCliente = nomeCliente
        self.__cpf = cpf
        self.__nascimento = nascimento
        self.__email = email
        self.__endereco = endereco
        self.__bairro = bairro
        self.__n_rua = n_rua
        self.__telefone = telefone

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def nomeCliente(self):
        return self.__nomeCliente

    @nomeCliente.setter
    def nomeCliente(self, nomeCliente):
        self.__nomeCliente = nomeCliente

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
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def bairro(self):
        return self.__bairro

    @bairro.setter
    def bairro(self, bairro):
        self.__bairro = bairro

    @property
    def n_rua(self):
        return self.__n_rua

    @n_rua.setter
    def n_rua(self, n_rua):
        self.__n_rua

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    def __str__(self) -> str:
        return self.__nomeCliente
