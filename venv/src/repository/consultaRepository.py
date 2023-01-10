from src.config.database import Conexao, psycopg2


class ConsultaRepository:
    def repositoryConsulta(idConsulta, dataConsulta, horarioConsulta, pagamento, observacao, animal, funcionario):

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

            def buscarIdFuncionario():
                sqlBuscarFuncionario = "SELECT id from funcionario where nome= %s"
                valor = funcionario
                cursor.execute(sqlBuscarFuncionario, (valor,))
                resultadoBuscaFuncionario = cursor.fetchone()
                for resultadoIdFuncionario in resultadoBuscaFuncionario:
                    return resultadoIdFuncionario

            animalId = BuscarIdAnimal()
            funcionarioId = buscarIdFuncionario()

            sql = "insert into agendamento(data, horario, pagamento, observação, animalid, funcionarioid) values( %s, %s, %s, %s, %s, %s)"
            valores = (dataConsulta, horarioConsulta, pagamento,
                       observacao, funcionarioId, animalId)
            cursor.execute(sql, valores)
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readConsultaRepository(animal):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlReadRepository = "select from agendamento where id=%s"
            valor = animal
            cursor.execute(sqlReadRepository, (valor,))
            readConsulta = cursor.fetchall()

            for consulta in readConsulta:
                print(consulta)
                return consulta
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def deleteConsultaRepository(consulta):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlDeleteConsulta = "delete from agendamento where id=%s"
            valor = consulta
            cursor.execute(sqlDeleteConsulta, (valor,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def UpdateConsultaRepository(animal):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            pass

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
