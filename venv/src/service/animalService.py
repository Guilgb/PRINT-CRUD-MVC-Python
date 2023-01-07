from src.repository.animalRepository import AnimalRepository


class AnimalService:

    def serviceAnimal(animal):
        id = int(animal.id)
        nomeAnimal = str(animal.nomeAnimal)
        especie = str(animal.especie)
        sexo = str(animal.sexo)
        raca = str(animal.raca)
        peso = float(animal.peso)
        nascimento = str(animal.nascimento)
        cliente = int(animal.cliente.idCliente)
        AnimalRepository.repositoryAnimal(
            id, nomeAnimal, especie, sexo, raca, peso, nascimento, cliente)
