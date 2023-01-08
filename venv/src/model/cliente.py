class Cliente:
    def __init__(self, idCliente: int, nomeCliente: str, cpf: str, nascimentoCliente: str,
                 email: str, endereco: str, bairro: str, n_rua: int, telefone: str):
        self.__idCliente = idCliente
        self.__nomeCliente = nomeCliente
        self.__cpf = cpf
        self.__nascimentoCliente = nascimentoCliente
        self.__email = email
        self.__endereco = endereco
        self.__bairro = bairro
        self.__n_rua = n_rua
        self.__telefone = telefone

    @property
    def idCliente(self):
        return self.__idCliente

    @idCliente.setter
    def idCliente(self, idCliente):
        self.__idCliente = idCliente

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
    def nascimentoCliente(self):
        return self.__nascimentoCliente

    @nascimentoCliente.setter
    def nascimentoCliente(self, nascimentoCliente):
        self.__nascimentoCliente = nascimentoCliente

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
