from src.model.cliente import Cliente
from src.service.clienteService import ClienteService


class ClienteController:
    def controllerCliente(cliente: Cliente):
        ClienteService.serviceCliente(cliente)

    def readClienteController(clinte: Cliente):
        ClienteService.readClienteService(clinte)

    def readAllClientesController(self):
        return ClienteService.readAllClientesService('')

    def deleteClienteController(cliente):
        ClienteService.deleteClienteService(cliente)

    def updateClienteController(cliente: Cliente):
        Cliente.updateClienteService(cliente)
