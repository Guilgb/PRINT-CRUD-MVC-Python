from src.repository.funcionarioRepository import FuncionarioRepository


class FuncionarioService:
    def serviceFuncionario(funcionario):
        FuncionarioRepository.repositoryFuncionario(funcionario)
