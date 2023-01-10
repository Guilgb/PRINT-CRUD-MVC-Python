from src.model.consulta import Consulta
from src.service.consultaService import ConsultaService


class ConsultaController:
    def controllerConsulta(agendamento: Consulta):
        ConsultaService.serviceConsulta(agendamento)

    def readConsultaController(consulta: Consulta):
        ConsultaService.readConsultaService(consulta)

    def deleteConsultaController(consulta: Consulta):
        ConsultaService.deleteConsultaService(consulta)

    def updateConsultaController(consulta: Consulta):
        ConsultaService.updateConsultaService(consulta)
