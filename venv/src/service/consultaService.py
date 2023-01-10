from src.repository.consultaRepository import ConsultaRepository
from datetime import datetime


class ConsultaService:
    def serviceConsulta(consulta):
        idConsulta = int(consulta.idConsulta)
        dataConsulta = str(consulta.dataConsulta)
        horarioConsulta = str(consulta.horario)
        pagamento = str(consulta.pagamento)
        observacao = str(consulta.observacao)
        animal = str(consulta.animal.nomeAnimal)
        funcionario = str(consulta.funcionario.nomeFuncionario)

        paraData = datetime.strptime(horarioConsulta, "%d-%b-%Y-%H:%M:%S")

        ConsultaRepository.repositoryConsulta(
            idConsulta, dataConsulta, paraData, pagamento, observacao,
            animal, funcionario)

    def readConsultaService(consulta):
        idConsulta = int(consulta.idConsulta)
        ConsultaRepository.readConsultaRepository(idConsulta)

    def deleteConsultaService(consulta):
        idConsulta = int(consulta.idConsulta)
        ConsultaRepository.deleteConsultaRepository(idConsulta)

    def updateConsultaService(consulta):
        pass
