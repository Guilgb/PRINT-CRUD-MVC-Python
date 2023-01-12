from src.service.vacinaService import VacinaService
from src.model.vacina import Vacina


class VacinaController:
    def controllerVacina(vacina: Vacina):
        VacinaService.serviceVacina(vacina)

    def readVacinaontroller(vacina):
        VacinaService.readVacinaService(vacina)

    def deleteVacinaController(vacina):
        VacinaService.deleteVacinaService(vacina)

    def updateVacinaController(vacina):
        VacinaService.updateVacinaService(vacina)
