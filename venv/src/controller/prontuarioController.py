from src.model.prontuario import Prontuario
from src.service.prontuarioService import ProntuarioService


class ProntuarioController:
    def controllerProntuario(prontuario: Prontuario):
        ProntuarioService.serviceProntuario(prontuario)
