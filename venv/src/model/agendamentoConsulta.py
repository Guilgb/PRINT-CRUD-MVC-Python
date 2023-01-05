class AgentamentoConsulta:
    def __init__(self, id: int, data: str, horario: str, telefoneAg: str,
                 pagemento: str, observacao: str):
        self.__id = id
        self.__data = data
        self.__horario = horario
        self.__telefoneAg = telefoneAg
        self.__pagemento = pagemento
        self.__observacao = observacao

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

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
