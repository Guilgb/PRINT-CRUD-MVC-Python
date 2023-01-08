from src.config.database import Conexao


class ClientRepository:
    def repositoryCliente(id, nomeCliente, cpf, nascimentoCliente,
                          telefoneCliente, email, rua, bairro, n_rua):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        # sql = "insert into cliente (nome, cpf, nascimento, telefone, email, rua, bairro, numero) values(%s, %s, %s, %s, %s, %s, %s, %s);"
        # value = (nomeCliente, cpf, nascimentoCliente, telefoneCliente, email,
        #          rua, bairro, n_rua)
        # cursor.execute(sql, value)
        # con.commit()
