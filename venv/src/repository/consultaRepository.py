from src.config.database import Conexao, psycopg2
from datetime import datetime


class ConsultaRepository:
    def repositoryConsulta(idConsulta, dataConsulta, horarioConsulta, observacao, animal, funcionario):

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

            sql = "insert into agendamento(data, horario, observação, animalid, funcionarioid) values( %s, %s, %s, %s, %s)"
            valores = (dataConsulta, horarioConsulta,
                       observacao, animalId, funcionarioId)
            cursor.execute(sql, valores)
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readConsultaRepository(self):

        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()
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
            valor = consulta
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

            sqlUpdateConsulta = "update agendamento set data=%s, horario=%s, observação=%s, animalid=%s, funcionarioid=%s"
            hora = datetime.strptime(consulta.horario, "%d-%b-%Y-%H:%M:%S")

            cursor.execute(sqlUpdateConsulta, (consulta.dataConsulta, hora,
                                               consulta.observacao, consulta.animal, consulta.funcionario))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
