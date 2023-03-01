from src.repository.animalRepository import AnimalRepository


class AnimalService:

    def serviceAnimal(animal):
        nomeAnimal = str(animal.nomeAnimal)
        especie = str(animal.especie)
        sexo = str(animal.sexo)
        raca = str(animal.raca)
        peso = animal.peso
        nascimento = str(animal.nascimento)
        cliente = str(animal.cliente)
        AnimalRepository.repositoryAnimal(
            nomeAnimal, especie, sexo, raca, peso, nascimento, cliente)

    def readServiceAnimal(self):
        return AnimalRepository.readRepositoryAnimal('')

    def deleServiceAnimal(animal):
        AnimalRepository.deleteRepositoryAnimal(animal)

    def updateServiceAnimal(animal):
        AnimalRepository.updateRepositoryAnimal(animal)
