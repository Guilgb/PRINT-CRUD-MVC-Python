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

        ProntuarioRepository.repositoryProntuario(
            idProntuario, sexo, porte, especie, dataProntuario, racaProntuario, animal, veterinario)

    def readProntuarioService(self):
        return ProntuarioRepository.readProntuarioRepository('')

    def deleteProntuarioService(prontuario):
        ProntuarioRepository.deleteProntuarioRepository(prontuario)

    def updateProntuarioService(prontuario):
        ProntuarioRepository.updateProntuarioRepository(prontuario)
