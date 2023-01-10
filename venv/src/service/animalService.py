from src.repository.animalRepository import AnimalRepository


class AnimalService:

    def serviceAnimal(animal):
        nomeAnimal = str(animal.nomeAnimal)
        especie = str(animal.especie)
        sexo = str(animal.sexo)
        raca = str(animal.raca)
        peso = float(animal.peso)
        nascimento = str(animal.nascimento)
        cliente = str(animal.cliente.nomeCliente)
        AnimalRepository.repositoryAnimal(
            nomeAnimal, especie, sexo, raca, peso, nascimento, cliente)

    def readServiceAnimal(animal):
        id = int(animal.id)
        AnimalRepository.readRepositoryAnimal(id)
