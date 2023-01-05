from src.repository.clienteRepository import ClientRepository


class ClienteService:
    def serviceCliente(cliente):
        ClientRepository.repositoryCliente(cliente)
