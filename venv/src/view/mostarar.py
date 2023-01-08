from src.model.animal import Animal
from src.model.cliente import Cliente
from src.model.consulta import Consulta
from src.model.funcionario import Funcionario
from src.model.prontuario import Prontuario
from src.model.vacina import Vacina
from src.model.veterinario import Veterinario

from src.controller.animalController import AnimalController
from src.controller.clienteController import ClienteController
from src.controller.consultaController import ConsultaController
from src.controller.funcionarioController import FuncionarioController
from src.controller.prontuarioController import ProntuarioController
from src.controller.vacinaController import VacinaController
from src.controller.veterinarioController import VeterinarioController

cliente = Cliente(1, 'Guilherme1', 'cpf6', 'nas6', 'tel6',
                  'mail6', 'rua6', 'num6', '6')
clienteControle = ClienteController.controllerCliente(cliente)

animal = Animal(1, 'Nome Animal', 'especie', 'sexo',
                'raca', 12.3, 'nascimento', cliente)

animalController = AnimalController.controllerAnimal(animal)

funcionario = Funcionario(1, 'nome', 'nascimento',
                          'email', 'telefone', 'cargo')

funcionarioController = FuncionarioController.controllerFuncionario(
    funcionario)
