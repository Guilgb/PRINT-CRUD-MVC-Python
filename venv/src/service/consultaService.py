from src.repository.consultaRepository import ConsultaRepository


class ConsultaService:
    def serviceConsulta(agendamento):
        idConsulta = str(agendamento.idConsulta)
        dataConsulta = str(agendamento.dataConsulta)
        horarioConsulta = str(agendamento.horario)
        pagamento = float(agendamento.pagamento)
        observacao = str(agendamento.observacao)
        animal = int(agendamento.animal.id)
        funcionario = int(agendamento.funcionario.idFuncionario)

        ConsultaRepository.repositoryConsulta(
            idConsulta, dataConsulta, horarioConsulta, pagamento, observacao,
            animal, funcionario)
