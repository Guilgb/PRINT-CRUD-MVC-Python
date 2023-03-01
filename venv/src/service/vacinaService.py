from src.repository.vacinaRepository import VacinaRepository


class VacinaService:
    def serviceVacina(vacina):
        idVacina = int(vacina.idVacina)
        nomeVacina = str(vacina.nomeVacina)
        fabricanteVacina = str(vacina.fabricante)
        validade = str(vacina.validade)
        volume = str(vacina.volume)
        VacinaRepository.repositoryVacina(
            idVacina, nomeVacina, fabricanteVacina, validade, volume)

    def readVacinaService(vacina):
        VacinaRepository.readVacinaRepository()

    def readAllVacinaSerice(self):
        return VacinaRepository.readAllRepositoryVacina('')

    def deleteVacinaService(vacina):
        VacinaRepository.deleteVacinaRepository(vacina)

    def updateVacinaService(vacina):
        VacinaRepository.updateVacinaRepository(vacina)
