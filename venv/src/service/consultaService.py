from src.repository.consultaRepository import ConsultaRepository
from datetime import datetime


class ConsultaService:
    def serviceConsulta(consulta):
        idConsulta = int(consulta.idConsulta)
        dataConsulta = str(consulta.dataConsulta)
        horarioConsulta = str(consulta.horario)
        pagamento = str(consulta.pagamento)
        observacao = str(consulta.observacao)
        animal = str(consulta.animal)
        funcionario = str(consulta.funcionario)
        ConsultaRepository.repositoryConsulta(
            idConsulta, dataConsulta, horarioConsulta, pagamento, observacao,
            animal, funcionario)

    def readConsultaService(self):
        return ConsultaRepository.readConsultaRepository(self)

    def deleteConsultaService(consulta):
        ConsultaRepository.deleteConsultaRepository(consulta)

    def updateConsultaService(consulta):
        ConsultaRepository.UpdateConsultaRepository(consulta)
