from src.model.animal import Animal
from src.service.animalService import AnimalService


class AnimalController:
    def controllerAnimal(animal: Animal):
        AnimalService.serviceAnimal(animal)

    def readControllerAimal(animal: Animal):
        AnimalService.readServiceAnimal(animal)

    def deleteControllerAnimal(animal: Animal):
        pass

    def updateControllerAnimal(animal: Animal):
        pass
