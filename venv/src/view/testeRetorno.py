from src.model.cliente import Cliente
from src.controller.clienteController import ClienteController

cliente = Cliente(1, 'nome Cliente', '127983712938719', '29/09/89',
                  'email@email.com', 'endereco', 'bairro', 'rua', 'telefone')

clienteController = ClienteController.controllerCliente(cliente)
