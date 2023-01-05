from src.model.animal import Animal
from src.repository.animalRepository import AnimalRepository


class AnimalService:

    def serviceAnimal(animal: Animal):
        if (animal.nomeAnimal == "Piroquinha"):
            AnimalRepository.repositoryAnimal(animal)
        else:
            print('Acesso negado')
