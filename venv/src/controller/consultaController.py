from src.model.consulta import Consulta
from src.service.consultaService import ConsultaService


class ConsultaController:
    def controllerConsulta(agendamento: Consulta):
        ConsultaService.serviceConsulta(agendamento)

    def readConsultaController(self):
        return ConsultaService.readConsultaService(self)

    def deleteConsultaController(consulta):
        ConsultaService.deleteConsultaService(consulta)

    def updateConsultaController(consulta):
        ConsultaService.updateConsultaService(consulta)
