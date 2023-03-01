from src.repository.clienteRepository import ClientRepository


class ClienteService:
    def serviceCliente(cliente):
        id = int(cliente.idCliente)
        nomeCliente = str(cliente.nomeCliente)
        cpf = str(cliente.cpf)
        nascimentoCliente = str(cliente.nascimentoCliente)
        email = str(cliente.email)
        endereco = str(cliente.rua)
        bairro = str(cliente.bairro)
        rua = str(cliente.n_rua)
        telefoneCliente = str(cliente.telefone)

        ClientRepository.repositoryCliente(
            id, nomeCliente, cpf, nascimentoCliente, email, endereco, bairro,
            rua, telefoneCliente)

    def readClienteService(cliente):
        id = int(cliente.idCliente)
        ClientRepository.readRepositoryCliente(id)

    def readAllClientesService(self):
        return ClientRepository.readAllClientesRepository('')

    def deleteClienteService(cliente):
        ClientRepository.deleteRepositoryCliente(cliente)

    def updateClienteService(cliente):
        ClientRepository.updateRepositoryCliente(cliente)
