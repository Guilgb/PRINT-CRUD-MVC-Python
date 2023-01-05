from src.repository.prontuarioRepository import ProntuarioRepository


class ProntuarioService:
    def serviceProntuario(prontuario):
        ProntuarioRepository.repositoryProntuario(prontuario)
