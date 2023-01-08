from src.config.database import Conexao


class ClientRepository:
    def repositoryCliente(id, nomeCliente: str, cpf, nascimentoCliente, email, endereco, bairro, rua, telefoneCliente):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        sql = "insert into cliente (nome, cpf, nascimento, telefone, email, rua, bairro, numero) values(%s, %s, %s, %s, %s, %s, %s, %s);"
        value = (nomeCliente, cpf, nascimentoCliente, email,
                 endereco, bairro, rua, telefoneCliente)
        cursor.execute(sql, value)
        con.commit()
