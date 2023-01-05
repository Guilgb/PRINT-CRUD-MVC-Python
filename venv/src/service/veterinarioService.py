from src.repository.veterinarioRepository import VeterinarioRepository


class VeterinarioService:
    def serviceVeterinario(veterinario):
        if (veterinario.nome == None):
            VeterinarioRepository.repositoryVeterinario(veterinario)
        else:
            print('Veterinário não existe!')
