from src.config.database import Conexao, psycopg2


class AnimalRepository:

    def repositoryAnimal(nomeAnimal, especie, sexo, raca, peso, nascimento, cliente):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            def buscarIdCliente():
                sqlBuscarCliente = "SELECT id FROM cliente WHERE nome = %s"
                valor = cliente
                cursor.execute(sqlBuscarCliente, (valor,))
                resultadoBusca = cursor.fetchone()

                for resultado in resultadoBusca:
                    return resultado

            resultadoFinal = buscarIdCliente()
            sql = "insert into animal (nome, especie, sexo, raca, peso, nascimento, clienteId) values(%s, %s, %s, %s, %s, %s, %s);"
            value = (nomeAnimal, especie, sexo,
                     raca, peso, nascimento, resultadoFinal)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readRepositoryAnimal(animalId):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlReadAnimal = "select * from animal "
            cursor.execute(sqlReadAnimal)
            resultadoReadAnimal = cursor.fetchall()

            for readAnimal in resultadoReadAnimal:
                print(readAnimal)
                return readAnimal

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()
