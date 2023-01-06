from src.model.funcionario import Funcionario
from src.model.animal import Animal


class AgentamentoConsulta(Funcionario):
    def __init__(self, idConsulta: int, dataConsulta: str, horario: str,
                 pagemento: str, observacao: str, idFuncionario: int, nomeFuncionario: str, nascimentoFuncionario: str, emailFuncionario: str, telefoneFuncionario: str, cargo: str, id: int, nomeAnimal: str, especie: str, sexo: str,
                 raca: str, peso: float, nascimento: str,  idCliente: int,
                 nomeCliente: str, cpf: str, nascimentoCliente: str,
                 email: str, endereco: str, bairro: str, n_rua: int,
                 telefone: str):

        super().__init__(idFuncionario, nomeFuncionario, nascimentoFuncionario,
                         emailFuncionario, telefoneFuncionario, cargo, Animal.__init__(id, nomeAnimal, especie, sexo,
                                                                                       raca, peso, nascimento,  idCliente,
                                                                                       nomeCliente, cpf, nascimentoCliente,
                                                                                       email, endereco, bairro, n_rua,
                                                                                       telefone))

        self.__idConsulta = idConsulta
        self.__dataConsulta = dataConsulta
        self.__horario = horario
        self.__pagemento = pagemento
        self.__observacao = observacao

    @property
    def idConsulta(self):
        return self.__idConsulta

    @idConsulta.setter
    def idConsulta(self, idConsulta):
        self.__idConsulta = idConsulta

    @property
    def dataConsulta(self):
        return self.__dataConsulta

    @dataConsulta.setter
    def dataConsulta(self, dataConsulta):
        self.__dataConsulta = dataConsulta

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, horario):
        self.__horario = horario

    @property
    def telefoneAg(self):
        return self.__telefoneAg

    @telefoneAg.setter
    def telefoneAg(self, telefoneAg):
        self.__telefoneAg = telefoneAg

    @property
    def pagemento(self):
        return self.__pagemento

    @pagemento.setter
    def pagemento(self, pagemento):
        self.__pagemento = pagemento

    @property
    def observacao(self):
        return self.__observacao

    @observacao.setter
    def observacao(self, observacao):
        self.__observacao = observacao

    def __str__(self) -> str:
        return self.observacao
