from src.model.cliente import Cliente
from src.repository.clienteRepository import ClientRepository


class ClienteService:
    def serviceCliente(cliente: Cliente):
        ClientRepository.repositoryCliente(cliente)
