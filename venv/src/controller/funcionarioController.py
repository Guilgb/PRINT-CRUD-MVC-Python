from src.model.funcionario import Funcionario
from src.service.funcionarioService import FuncionarioService


class FuncionarioController:
    def controllerFuncionario(funcionario: Funcionario):
        FuncionarioService.serviceFuncionario(funcionario)

    def readFucionarioController(self):
        return FuncionarioService.serviceReadFuncionario(self)

    def deleteFuncionarioController(funcionario):
        FuncionarioService.serviceDeleteFuncionario(funcionario)

    def updateFuncionarioController(funcionario):
        FuncionarioService.serviceUpdateFuncionario(funcionario)
