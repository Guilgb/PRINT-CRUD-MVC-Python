from src.model.prontuario import Prontuario
from src.service.prontuarioService import ProntuarioService


class ProntuarioController:
    def controllerProntuario(prontuario: Prontuario):
        ProntuarioService.serviceProntuario(prontuario)

    def readProntuarioontroller(prontuario):
        ProntuarioService.readProntuarioService(prontuario)

    def deleteProntuarioController(prontuario):
        ProntuarioService.deleteProntuarioService(prontuario)

    def updateProntuarioController(prontuario):
        ProntuarioService.updateProntuarioService(prontuario)
