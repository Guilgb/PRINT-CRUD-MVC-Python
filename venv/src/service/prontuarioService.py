from src.repository.prontuarioRepository import ProntuarioRepository


class ProntuarioService:
    def serviceProntuario(prontuario):
        idProntuario = int(prontuario.idProntuario)
        sexo = str(prontuario.sexo)
        porte = str(prontuario.porte)
        especie = str(prontuario.especie)
        dataProntuario = str(prontuario.dataProntuario)
        racaProntuario = str(prontuario.racaProntuario)
        animal = int(prontuario.animal.id)
        veterinario = int(prontuario.veterinario.idVeterinario)

        ProntuarioRepository.repositoryProntuario(
            idProntuario, sexo, porte, especie, dataProntuario, racaProntuario, animal, veterinario)
