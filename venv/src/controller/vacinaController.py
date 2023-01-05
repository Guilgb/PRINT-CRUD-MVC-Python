from src.service.vacinaService import VacinaService
from src.model.vacina import Vacina


class VacinaController:
    def controllerVacina(vacina: Vacina):
        VacinaService.serviceVacina(vacina)
