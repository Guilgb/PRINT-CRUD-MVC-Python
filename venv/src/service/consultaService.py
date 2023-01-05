from src.model.agendamentoConsulta import AgentamentoConsulta
from src.repository.consultaRepository import ConsultaRepository


class ConsultaService:
    def serviceConsulta(agedamento: AgentamentoConsulta):
        ConsultaRepository.repositoryConsulta(agedamento)
