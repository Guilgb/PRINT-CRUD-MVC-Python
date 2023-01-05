from src.repository.consultaRepository import ConsultaRepository


class ConsultaService:
    def serviceConsulta(agedamento):
        ConsultaRepository.repositoryConsulta(agedamento)
