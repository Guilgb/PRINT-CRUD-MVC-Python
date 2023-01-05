from src.model.agendamentoConsulta import AgentamentoConsulta
from src.service.consultaService import ConsultaService


class ConsultaController:
    def controllerConsulta(agendamento: AgentamentoConsulta):
        ConsultaService.serviceConsulta(agendamento)
