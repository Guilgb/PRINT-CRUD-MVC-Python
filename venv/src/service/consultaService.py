from src.repository.consultaRepository import ConsultaRepository


class ConsultaService:
    def serviceConsulta(agendamento):
        idConsulta = str(agendamento.idConsulta)
        dataConsulta = str(agendamento.dataConsulta)
        horarioConsulta = str(agendamento.horario)
        pagamento = str(agendamento.pagamento)
        observacao = str(agendamento.observacao)
        animal = str(agendamento.animal.nomeAnimal)
        funcionario = str(agendamento.funcionario.nomeFuncionario)

        ConsultaRepository.repositoryConsulta(
            idConsulta, dataConsulta, horarioConsulta, pagamento, observacao,
            animal, funcionario)
