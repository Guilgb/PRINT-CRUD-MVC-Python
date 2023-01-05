from src.repository.animalRepository import AnimalRepository


class AnimalService:

    def serviceAnimal(animal):
        if (animal.nomeAnimal == "Piroquinha"):
            AnimalRepository.repositoryAnimal(animal)
        else:
            print('Acesso negado')
