from src.model.animal import Animal
from src.model.cliente import Cliente
from src.model.agendamentoConsulta import AgentamentoConsulta
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

cliente = Cliente(2, 'Guilherme', '07341965398', '28/01/1999',
                  'guilherme.gb@hotmail.com', '63400000', 'Centro', 'Av. Pedro Lopes', '88996431916')
animal = Animal(1, 'Piroquinhas', 'Felino', 'M',
                'Cianes', 1.2, '20/08/2020', '88999771125', cliente.nomeCliente, cliente.cpf, cliente.nascimentoCliente, cliente.email, cliente.endereco, cliente.bairro, cliente.n_rua, cliente.telefone)
agendamento = AgentamentoConsulta(
    3, '05/01/2023', '13:24', '88996431916', '2000127987189410871', 'Agendamento de Consulta')
funcionario = Funcionario(1, 'Nome Funcionario', '20/06/2018',
                          'email@funcionario.com', '9988776676', 'Funcionario')
prontuario = Prontuario(1, 'M', 'Porte', 'Especie', '22/01/2020', 'Cianes')

vacina = Vacina(1, 'VaXina', 'Xina', '28/08/2023', '30L')

veterinario = Veterinario(1, 'Dr. Rubens', '09876543287',
                          '12/12/1212', '889982328923', 'rubens@gmail.com', 'sistemas de informação')

clienteControle = ClienteController.controllerCliente(cliente)
animalControle = AnimalController.controllerAnimal(animal)
agendamentoControle = ConsultaController.controllerConsulta(agendamento)
funcionarioControle = FuncionarioController.controllerFuncionario(funcionario)
prontuarioControle = ProntuarioController.controllerProntuario(prontuario)
vacinaControle = VacinaController.controllerVacina(vacina)
VeterinarioController = VeterinarioController.controllerVeterinario(
    veterinario)
