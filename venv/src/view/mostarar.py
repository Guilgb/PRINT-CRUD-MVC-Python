from src.model.animal import Animal
from src.model.cliente import Cliente
from src.model.agendamentoConsulta import AgentamentoConsulta
from src.model.funcionario import Funcionario
from src.model.prontuario import Prontuario

from src.controller.animalController import AnimalController
from src.controller.clienteController import ClienteController
from src.controller.consultaController import ConsultaController
from src.controller.funcionarioController import FuncionarioController
from src.controller.prontuarioController import ProntuarioController

animal = Animal(1, 'Piroquinhas', 'Felino', 'M', 'Cianes', 1.2, '20/08/2020')
cliente = Cliente(2, 'Guilherme', '07341965398', '28/01/1999',
                  'guilherme.gb@hotmail.com', '63400000', 'Centro', 'Av. Pedro Lopes', '88996431916')
agendamento = AgentamentoConsulta(
    3, '05/01/2023', '13:24', '88996431916', '2000127987189410871', 'Agendamento de Consulta')
funcionario = Funcionario(1, 'Nome Funcionario', '20/06/2018',
                          'email@funcionario.com', '9988776676', 'Funcionario')
prontuario = Prontuario(1, 'M', 'Porte', 'Especie', '22/01/2020', 'Cianes')


clienteControle = ClienteController.controllerCliente(cliente)
animalControle = AnimalController.controllerAnimal(animal)
agendamentoControle = ConsultaController.controllerConsulta(agendamento)
funcionarioControle = FuncionarioController.controllerFuncionario(funcionario)
prontuarioControle = ProntuarioController.controllerProntuario(prontuario)
