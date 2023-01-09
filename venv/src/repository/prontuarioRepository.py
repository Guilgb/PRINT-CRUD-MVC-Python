from src.config.database import Conexao, psycopg2


class ProntuarioRepository:
    def repositoryProntuario(idProntuario, sexo, porte, especie, dataProntuario, racaProntuario, animal, veterinario, vacina):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into prontuario(sexo, porte, especie, data, raca, animalid, veterinarioid)"
            value = (sexo, porte, especie, dataProntuario, racaProntuario)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
