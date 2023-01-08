from src.model.funcionario import Funcionario
from src.model.animal import Animal


class AgentamentoConsulta(Funcionario, Animal):
    def __init__(self, idConsulta: int, dataConsulta: str, horario: str,
                 pagamento: str, observacao: str,
                 animal: Animal, funcionario: Funcionario):

        self.__idConsulta = idConsulta
        self.__dataConsulta = dataConsulta
        self.__horario = horario
        self.__pagamento = pagamento
        self.__observacao = observacao
        self.__animal = animal
        self.__funcionario = funcionario

    @ property
    def idConsulta(self):
        return self.__idConsulta

    @ idConsulta.setter
    def idConsulta(self, idConsulta):
        self.__idConsulta = idConsulta

    @ property
    def dataConsulta(self):
        return self.__dataConsulta

    @ dataConsulta.setter
    def dataConsulta(self, dataConsulta):
        self.__dataConsulta = dataConsulta

    @ property
    def horario(self):
        return self.__horario

    @ horario.setter
    def horario(self, horario):
        self.__horario = horario

    @ property
    def pagamento(self):
        return self.__pagamento

    @ pagamento.setter
    def pagamento(self, pagamento):
        self.__pagamento = pagamento

    @ property
    def observacao(self):
        return self.__observacao

    @ observacao.setter
    def observacao(self, observacao):
        self.__observacao = observacao

    @ property
    def animal(self):
        return self.__animal

    @ animal.setter
    def animal(self, animal):
        self.__animal = animal

    @ property
    def funcionario(self):
        return self.__funcionario

    @ funcionario.setter
    def funcionario(self, funcionario):
        self.__funcionario = funcionario
