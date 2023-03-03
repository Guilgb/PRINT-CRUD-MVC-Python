from src.config.database import Conexao, psycopg2


class AnimalRepository:

    def repositoryAnimal(nomeAnimal, especie, sexo, raca, peso, nascimento, cliente):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into animal (nome, especie, sexo, raca, peso, nascimento, clienteId) values(%s, %s, %s, %s, %s, %s, %s);"
            value = (nomeAnimal, especie, sexo,
                     raca, peso, nascimento, cliente)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readRepositoryAnimal(self):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlReadAnimal = "select * from animal"
            cursor.execute(sqlReadAnimal)
            resultadoReadAnimal = cursor.fetchall()
            return resultadoReadAnimal

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def deleteRepositoryAnimal(animal):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()
            sqlDeleteAnimal = "delete from animal where id=%s"
            value = animal
            cursor.execute(sqlDeleteAnimal, (value,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def updateRepositoryAnimal(animal):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlDeleteAnimal = "update animal set nome=%s, especie=%s, sexo=%s, raca=%s, peso=%s, nascimento=%s, clienteid=%s where id=%s"
            cursor.execute(sqlDeleteAnimal, (animal.nomeAnimal, animal.especie,
                           animal.sexo, animal.raca, animal.peso,
                           animal.nascimento, animal.cliente, animal.id))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()
