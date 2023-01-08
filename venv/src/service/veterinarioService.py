from src.repository.veterinarioRepository import VeterinarioRepository


class VeterinarioService:
    def serviceVeterinario(veterinario):
        idVeterinario = int(veterinario.idVeterinario)
        nomeVeterinario = str(veterinario.nomeVeterinario)
        cpfVeterinario = str(veterinario.cpfVeterinario)
        nascimentoVeterinario = str(veterinario.nascimentoVeterinario)
        telefoneVeterinario = str(veterinario.telefoneVeterinario)
        emailVeterinario = str(veterinario.emailVeterinario)
        formacao = str(veterinario.formacao)

        VeterinarioRepository.repositoryVeterinario(
            idVeterinario, nomeVeterinario, cpfVeterinario,
            nascimentoVeterinario, telefoneVeterinario, emailVeterinario,
            formacao)
