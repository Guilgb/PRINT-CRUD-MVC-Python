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

cliente = Cliente(1, 'nome', 'cpf2', 'nas', 'tel', 'mail', 'rua', 'num', '')
clienteControle = ClienteController.controllerCliente(cliente)
