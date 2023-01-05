from src.repository.vacinaRepository import VacinaRepository


class VacinaService:
    def serviceVacina(vacina):
        VacinaRepository.repositoryVacina(vacina)
