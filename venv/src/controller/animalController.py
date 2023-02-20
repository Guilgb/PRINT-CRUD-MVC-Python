from src.model.animal import Animal
from src.service.animalService import AnimalService


class AnimalController:
    def controllerAnimal(animal: Animal):
        AnimalService.serviceAnimal(animal)

    def readControllerAimal(self):
        return AnimalService.readServiceAnimal('')

    def deleteControllerAnimal(animal):
        AnimalService.deleServiceAnimal(animal)

    def updateControllerAnimal(animal):
        AnimalService.updateServiceAnimal(animal)
