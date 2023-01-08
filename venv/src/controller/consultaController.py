from src.model.consulta import Consulta
from src.service.consultaService import ConsultaService


class ConsultaController:
    def controllerConsulta(agendamento: Consulta):
        ConsultaService.serviceConsulta(agendamento)
