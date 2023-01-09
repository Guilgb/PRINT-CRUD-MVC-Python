from src.config.database import Conexao, psycopg2


class VacinaRepository:
    def repositoryVacina(idVacina, nomeVacina, fabricanteVacina, validade, volume):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into vacina(nome, validade, fabricante, volume) values(%s, %s, %s, %s);"
            value = (nomeVacina, validade, fabricanteVacina, volume)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
