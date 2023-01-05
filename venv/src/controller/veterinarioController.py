from src.model.veterinario import Veterinario
from src.service.veterinarioService import VeterinarioService

class VeterinarioController:
  def controllerVeterinario(veterinario: Veterinario):
    VeterinarioService.serviceVeterinario(veterinario)