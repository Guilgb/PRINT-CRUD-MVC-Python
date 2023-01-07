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
animal = Animal(3, 'nomeAnimal', 'especie', 'sexo',
                'raca', 12.2, 'nascimento',  cliente)

funcionario = Funcionario(1, 'Nome Funcionario', '20/06/2018',
                          'email@funcionario.com', '9988776676', 'Funcionario')
agendamento = AgentamentoConsulta(
    10, 'data', 'horario', 'pagamento', 'observacao', animal, funcionario)
vacina = Vacina(1, 'VaXina', 'Xina', '28/08/2023', '30L')

veterinario = Veterinario(1, 'Dr. Rubens', '09876543287',
                          '12/12/1212', '889982328923', 'rubens@gmail.com', 'sistemas de informação')

prontuario = Prontuario(23, 'sexo', 'porte', 'especie',
                        'dataProntuario', 'racaProntuario', animal, veterinario)

clienteControle = ClienteController.controllerCliente(cliente)
animalControle = AnimalController.controllerAnimal(animal)
agendamentoControle = ConsultaController.controllerConsulta(agendamento)
funcionarioControle = FuncionarioController.controllerFuncionario(funcionario)
vacinaControle = VacinaController.controllerVacina(vacina)
pontuarioControle = ProntuarioController.controllerProntuario(prontuario)
VeterinarioController = VeterinarioController.controllerVeterinario(
    veterinario)
