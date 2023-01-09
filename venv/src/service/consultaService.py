from src.repository.consultaRepository import ConsultaRepository
from datetime import datetime


class ConsultaService:
    def serviceConsulta(agendamento):
        idConsulta = str(agendamento.idConsulta)
        dataConsulta = str(agendamento.dataConsulta)
        horarioConsulta = str(agendamento.horario)
        pagamento = str(agendamento.pagamento)
        observacao = str(agendamento.observacao)
        animal = str(agendamento.animal.nomeAnimal)
        funcionario = str(agendamento.funcionario.nomeFuncionario)

        paraData = datetime.strptime(horarioConsulta, "%d-%b-%Y-%H:%M:%S")

        ConsultaRepository.repositoryConsulta(
            idConsulta, dataConsulta, paraData, pagamento, observacao,
            animal, funcionario)
