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
clienteControle = ClienteController.controllerCliente(cliente)
