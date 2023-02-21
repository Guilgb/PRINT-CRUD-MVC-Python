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
                       observacao, animalId, funcionarioId)
            cursor.execute(sql, valores)
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readConsultaRepository(self):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlReadRepository = "select * from agendamento"
            cursor.execute(sqlReadRepository)
            readConsulta = cursor.fetchall()
            return readConsulta

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
            valor = consulta.idConsulta
            cursor.execute(sqlDeleteConsulta, (valor,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def UpdateConsultaRepository(consulta):

        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            def buscarIdAnimal():
                sqlBuscarAnimal = "SELECT id FROM animal WHERE nome = %s"
                valor = consulta.animal
                cursor.execute(sqlBuscarAnimal, (valor,))
                resultadoBusca = cursor.fetchone()

                for resultado in resultadoBusca:
                    return resultado
            AnimalId = buscarIdAnimal()

            def buscarIdFuncionario():
                sqlBuscarFuncionario = "SELECT id FROM funcionario WHERE nome = %s"
                valor = consulta.nomeAnimal
                cursor.execute(sqlBuscarFuncionario, (valor,))
                resultadoBusca = cursor.fetchone()

                for resultado in resultadoBusca:
                    return resultado
            FuncionarioId = buscarIdFuncionario()

            sqlUpdateConsulta = "update consulta set data=%s, horario=%s, pagamento=%s, observação=%s, animalid=%s, funcionarioid=%s"
            cursor.execute(sqlUpdateConsulta, (consulta.dataConsulta, consulta.horario,
                           consulta.horario, consulta.pagamento, consulta.observacao, AnimalId, FuncionarioId))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
