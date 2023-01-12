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
            idFuncionario, nomeFuncionario, nascimentoFuncionario, emailFuncionario, telefoneFuncionario, cargo)

    def serviceReadFuncionario(funcionario):
        idFuncionario = int(funcionario.idFuncionario)
        FuncionarioRepository.readFuncionarioRepository(idFuncionario)

    def serviceDeleteFuncionario(funcionario):
        idFuncionario = int(funcionario.idFuncionario)
        FuncionarioRepository.deleteFuncionarioRepository(idFuncionario)

    def serviceUpdateFuncionario(funcionario):
        pass
