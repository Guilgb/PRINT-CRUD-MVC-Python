from src.model.cliente import Cliente
from src.service.clienteService import ClienteService


class ClienteController:
    def controllerCliente(cliente: Cliente):
        ClienteService.serviceCliente(cliente)
