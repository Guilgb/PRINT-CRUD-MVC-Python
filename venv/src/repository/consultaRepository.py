from src.config.database import Conexao, psycopg2
from datetime import datetime


class ConsultaRepository:
    
    def repositoryConsulta(idConsulta, dataConsulta, horarioConsulta, observacao, animal, funcionario):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into agendamento(dia, momento, observação, animalid, funcionarioid) values( %s, %s, %s, %s, %s)"
            valores = (dataConsulta, horarioConsulta,
                       observacao, animal, funcionario)
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

            sqlUpdateConsulta = "update agendamento set dia=%s, momento=%s, observação=%s, animalid=%s, funcionarioid=%s"

            cursor.execute(sqlUpdateConsulta, (consulta.dataConsulta, consulta.horario,
                                               consulta.observacao, consulta.animal, consulta.funcionario))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
