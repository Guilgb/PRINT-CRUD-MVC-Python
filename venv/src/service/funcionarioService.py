from src.model.funcionario import Funcionario
from src.repository.funcionarioRepository import FuncionarioRepository


class FuncionarioService:
    def serviceFuncionario(funcionario: Funcionario):
        FuncionarioRepository.repositoryFuncionario(funcionario)
