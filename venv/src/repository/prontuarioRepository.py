from src.config.database import Conexao, psycopg2


class ProntuarioRepository:
    def repositoryProntuario(idProntuario, sexo, porte, especie, dataProntuario, racaProntuario, animal, veterinario, vacina):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            def BuscarIdAnimal():
                sqlBuscarAnimal = "SELECT id FROM animal where nome = %s"
                valor = animal
                cursor.execute(sqlBuscarAnimal, (valor,))
                resultadoAnimal = cursor.fetchone()

                for idanimal in resultadoAnimal:
                    return idanimal

            def BuscarIdVet():
                sqlBuscarvet = "SELECT id FROM veterinario where nome = %s"
                valorVet = veterinario
                cursor.execute(sqlBuscarvet, (valorVet,))
                resultadoVet = cursor.fetchone()

                for idVet in resultadoVet:
                    return idVet

            animalId = BuscarIdAnimal()
            vetId = BuscarIdVet()

            sql = "insert into prontuario(sexo, porte, especie, data, raca, animalid, veterinarioid) values(%s, %s, %s, %s, %s, %s, %s)"
            value = (sexo, porte, especie, dataProntuario,
                     racaProntuario, animalId, vetId)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readProntuarioRepository(prontuario):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlReadProntuario = "select from prontuario where id=%s"
            valor = prontuario
            cursor.execute(sqlReadProntuario, (valor,))
            readFuncionario = cursor.fetchall()

            for funcionario in readFuncionario:
                print(prontuario)
                return prontuario
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def deleteProntuarioRepository(prontuario):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlDeleteProntuario = "delete from prontuario where id=%s"
            valor = prontuario
            cursor.execute(sqlDeleteProntuario, (valor,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def updateProntuarioRepository(prontuario):
        pass
