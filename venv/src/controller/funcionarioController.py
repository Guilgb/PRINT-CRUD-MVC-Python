from src.model.funcionario import Funcionario
from src.service.funcionarioService import FuncionarioService


class FuncionarioController:
    def controllerFuncionario(funcionario: Funcionario):
        FuncionarioService.serviceFuncionario(funcionario)
