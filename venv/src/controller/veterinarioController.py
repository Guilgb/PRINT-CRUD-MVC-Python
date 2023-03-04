from src.model.veterinario import Veterinario
from src.service.veterinarioService import VeterinarioService


class VeterinarioController:
    def controllerVeterinario(veterinario: Veterinario):
        VeterinarioService.serviceVeterinario(veterinario)

    def readControllerVeterinario(self):
        return VeterinarioService.readServiceVeterinario('')

    def deleteControllerVeterinario(veterinario):
        VeterinarioService.deleteServiceVeterinario(veterinario)

    def updateControllerVeterinario(veterinario):
        VeterinarioService.updateServiceVeterinario(veterinario)
