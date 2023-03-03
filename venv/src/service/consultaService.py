from src.repository.consultaRepository import ConsultaRepository
from datetime import datetime


class ConsultaService:
    def serviceConsulta(consulta):
        idConsulta = int(consulta.idConsulta)
        dataConsulta = str(consulta.dataConsulta)
        horarioConsulta = str(consulta.horario)
        observacao = str(consulta.observacao)
        animal = consulta.animal
        funcionario = consulta.funcionario
        ConsultaRepository.repositoryConsulta(
            idConsulta, dataConsulta, horarioConsulta, observacao,
            animal, funcionario)

    def readConsultaService(self):
        return ConsultaRepository.readConsultaRepository(self)

    def deleteConsultaService(consulta):
        ConsultaRepository.deleteConsultaRepository(consulta)

    def updateConsultaService(consulta):
        ConsultaRepository.UpdateConsultaRepository(consulta)
