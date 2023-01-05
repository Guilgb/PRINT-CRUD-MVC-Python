from src.model.veterinario import Veterinario
from src.repository.veterinarioRepository import VeterinarioRepository

class VeterinarioService:
  def serviceVeterinario(veterinario: Veterinario):
    if(veterinario.nome == None):
      VeterinarioRepository.repositoryVeterinario(veterinario)
    else:
      print('Veterinário não existe!')
