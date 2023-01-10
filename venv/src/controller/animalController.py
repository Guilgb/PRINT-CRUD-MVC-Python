from src.model.animal import Animal
from src.service.animalService import AnimalService


class AnimalController:
    def controllerAnimal(animal: Animal):
        AnimalService.serviceAnimal(animal)

    def readAnimal(animal: Animal):
        AnimalService.readServiceAnimal(animal)
