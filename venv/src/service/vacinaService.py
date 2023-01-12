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
        idVacina = int(vacina.idVacina)
        VacinaRepository.readVacinaRepository(idVacina)

    def deleteProntuarioService(vacina):
        idVacina = int(vacina.idVacina)
        VacinaRepository.deleteVacinaRepository(idVacina)

    def updateVacinaService(vacina):
        pass
