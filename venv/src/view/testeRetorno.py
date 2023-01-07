from src.model.cliente import Cliente
from src.controller.clienteController import ClienteController
from src.model.animal import Animal
from src.controller.animalController import AnimalController

cliente = Cliente(1, 'nome Cliente', '127983712938719', '29/09/89',
                  'email@email.com', 'endereco', 'bairro', 'rua', 'telefone')

animal = Animal(3, 'nomeAnimal', 'especie', 'sexo',
                'raca', 12.2, 'nascimento',  cliente)

clienteController = ClienteController.controllerCliente(cliente)
animalControle = AnimalController.controllerAnimal(animal)
