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

    def readVacinaRepository(vacina):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlReadVacina = "select from vacina where id=%s"
            valor = vacina.idVacina
            cursor.execute(sqlReadVacina, (valor,))
            readVacina = cursor.fetchall()

            for vacinas in readVacina:
                return vacinas
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readAllRepositoryVacina(vacinaId):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlReadVacina = "select * from vacina"
            cursor.execute(sqlReadVacina)
            resultadoReadCliente = cursor.fetchall()
            return resultadoReadCliente

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def deleteVacinaRepository(vacina):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlDeleteVacina = "delete from vacina where id=%s"
            valor = vacina
            cursor.execute(sqlDeleteVacina, (valor,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def updateVacinaRepository(vacina):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            def buscarIdVacina():
                sqlBuscarCliente = "SELECT id FROM vacina WHERE nome = %s"
                valor = vacina.nomeVacina
                cursor.execute(sqlBuscarCliente, (valor,))
                resultadoBusca = cursor.fetchone()

                for resultado in resultadoBusca:
                    return resultado

            vacinaId = buscarIdVacina()

            sqlUpateVacina = "update vacina set nome=%s, validade=%s, fabricante=%s, volume=%s where id=%s"
            cursor.execute(sqlUpateVacina, (vacina.nomeVacina,
                           vacina.validade, vacina.fabricante, vacina.volume, vacinaId))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()
