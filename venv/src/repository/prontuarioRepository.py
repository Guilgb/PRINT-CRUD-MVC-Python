from src.config.database import Conexao, psycopg2


class ProntuarioRepository:
    def repositoryProntuario(idProntuario, sexo, porte, especie, dataProntuario, racaProntuario, animal, veterinario):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into prontuario(sexo, porte, especie, data, raca, animalid, veterinarioid) values(%s, %s, %s, %s, %s, %s, %s)"
            value = (sexo, porte, especie, dataProntuario,
                     racaProntuario, animal, veterinario)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readProntuarioRepository(self):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlReadProntuario = "select * from prontuario"
            cursor.execute(sqlReadProntuario)
            readProntuario = cursor.fetchall()
            return readProntuario

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
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlUpateProntuario = "update prontuario set sexo=%s, porte=%s, especie=%s, data=%s, raca=%s, animalid=%s, veterinarioid=%s where id=%s"
            cursor.execute(sqlUpateProntuario, (prontuario.sexo, prontuario.porte, prontuario.especie, prontuario.dataProntuario, prontuario.racaProntuario, prontuario.animal, prontuario.veterinario, prontuario.idProntuario ))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()
