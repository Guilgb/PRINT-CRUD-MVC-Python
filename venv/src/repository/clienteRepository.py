from src.config.database import Conexao, psycopg2


class ClientRepository:
    def repositoryCliente(id, nomeCliente, cpf, nascimentoCliente,
                          telefoneCliente, email, rua, bairro, n_rua):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into cliente (nome, cpf, nascimento, telefone, email, rua, bairro, numero) values(%s, %s, %s, %s, %s, %s, %s, %s);"
            value = (nomeCliente, cpf, nascimentoCliente, telefoneCliente, email,
                     rua, bairro, n_rua)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readRepositoryCliente(clienteId):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlReadCliente = "select * from cliente where id=%s"
            value = (clienteId)
            cursor.execute(sqlReadCliente, (value,))
            resultadoReadCliente = cursor.fetchall()

            for readCliente in resultadoReadCliente:
                print(readCliente)
                return readCliente

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def deleteRepositoryCliente(cliente):

        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlDeleteCliente = "delete from cliente where id=%s"
            value = (clienteId)
            cursor.execute(sqlDeleteCliente, (value,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def updateRepositoryCliente(cliente):
        pass
