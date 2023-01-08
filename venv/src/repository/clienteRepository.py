from src.config.database import Conexao


class ClientRepository:
    def repositoryCliente(id, nomeCliente, cpf, nascimentoCliente, email, endereco, bairro, rua, telefoneCliente):

        print(id, nomeCliente, cpf, nascimentoCliente,
              email, endereco, bairro, rua, telefoneCliente)

        con = Conexao.getConnection('')
        cursor = con.cursor()

        sql = "insert into Cliente(nomeCliente) value(%s)"
        value = (nomeCliente)
        cursor.execute(sql, value)
        con.commit()
