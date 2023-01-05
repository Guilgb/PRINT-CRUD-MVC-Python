from src.model.prontuario import Prontuario
from src.repository.prontuarioRepository import ProntuarioRepository


class ProntuarioService:
    def serviceProntuario(prontuario: Prontuario):
        ProntuarioRepository.repositoryProntuario(prontuario)
