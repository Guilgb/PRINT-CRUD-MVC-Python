from src.repository.funcionarioRepository import FuncionarioRepository


class FuncionarioService:
    def serviceFuncionario(funcionario):
        idFuncionario = int(funcionario.idFuncionario)
        nomeFuncionario = str(funcionario.nomeFuncionario)
        nascimentoFuncionario = str(funcionario.nascimentoFuncionario)
        emailFuncionario = str(funcionario.emailFuncionario)
        telefoneFuncionario = str(funcionario.telefoneFuncionario)
        cargo = str(funcionario.cargo)

        FuncionarioRepository.insertFuncionario(
            idFuncionario, nomeFuncionario, nascimentoFuncionario,
            emailFuncionario, telefoneFuncionario, cargo)

    def serviceReadFuncionario(self):
        return FuncionarioRepository.readFuncionarioRepository(self)

    def serviceDeleteFuncionario(funcionario):
        FuncionarioRepository.deleteFuncionarioRepository(funcionario)

    def serviceUpdateFuncionario(funcionario):
        FuncionarioRepository.updateFuncionarioRepository(funcionario)
