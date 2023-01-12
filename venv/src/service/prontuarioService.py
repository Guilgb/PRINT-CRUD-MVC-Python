from src.repository.prontuarioRepository import ProntuarioRepository


class ProntuarioService:
    def serviceProntuario(prontuario):
        idProntuario = int(prontuario.idProntuario)
        sexo = str(prontuario.sexo)
        porte = str(prontuario.porte)
        especie = str(prontuario.especie)
        dataProntuario = str(prontuario.dataProntuario)
        racaProntuario = str(prontuario.racaProntuario)
        animal = str(prontuario.animal.nomeAnimal)
        veterinario = str(prontuario.veterinario.nomeVeterinario)
        vacina = str(prontuario.vacina.nomeVacina)

        ProntuarioRepository.repositoryProntuario(
            idProntuario, sexo, porte, especie, dataProntuario, racaProntuario, animal, veterinario, vacina)

    def readProntuarioService(prontuario):
        idProntuario = int(prontuario.idProntuario)
        ProntuarioRepository.readProntuarioRepository(idProntuario)

    def deleteProntuarioService(prontuario):
        idProntuario = int(prontuario.idProntuario)
        ProntuarioRepository.deleteProntuarioRepository(idProntuario)

    def updateProntuarioService(prontuario):
        pass
