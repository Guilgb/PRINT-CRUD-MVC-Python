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

# cliente = Cliente(1, 'a1', 'cpf9', 'nas8', 'tel8',
#                   'mail9', 'rua9', 'num9', '9')

# animal = Animal(1, 'ragavan', 'especi2', 'sex2',
#                 'raa2', 12.4, 'nasciment2', 'f')

# funcionario = Funcionario(1, 'nome', 'nascimento',
#                           'email', 'telefone', 'cargo')

consulta = Consulta(1, 'data', '30-May-2020-15:59:02', 'pagamento',
                    'obs', 'ragavan', 'nome')

# vacina = Vacina(1, 'nomeVacina', 'fabricante', 'vlidade', 'volume')

# vaterinario = Veterinario(1, 'vete', 'cpf', 'nas', 'tel', 'mail', 'medico vet')

# prontuario = Prontuario(1, 'S', 'P', 'E', 'Data', 'R',
#                         animal, vaterinario, vacina)

# clienteControle = ClienteController.deleteClienteController(cliente)
# animalController = AnimalController.controllerAnimal(animal)
# funcionarioController = FuncionarioController.controllerFuncionario(
#     funcionario)
ConsultaController.controllerConsulta(consulta)
# vacinaControlle = VacinaController.controllerVacina(vacina)
# veterinarioCont = VeterinarioController.controllerVeterinario(vaterinario)
# controlePro = ProntuarioController.controllerProntuario(prontuario)
