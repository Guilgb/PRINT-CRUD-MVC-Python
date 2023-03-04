from src.config.database import Conexao, psycopg2


class VeterinarioRepository:
    def repositoryVeterinario(idVeterinario, nomeVeterinario, cpfVeterinario,
                              nascimentoVeterinario,
                              telefoneVeterinario, emailVeterinario, formacao):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into veterinario(nome, cpf, nascimento, telefone, email, formacao) values(%s, %s, %s, %s, %s, %s)"
            value = (nomeVeterinario, cpfVeterinario, nascimentoVeterinario,
                     telefoneVeterinario, emailVeterinario, formacao)
            cursor.execute(sql, value)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def readVeterinarioRepository(self):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlReadRepository = "select * from veterinario"
            cursor.execute(sqlReadRepository)
            readVeterinario = cursor.fetchall()
            return readVeterinario

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def deleteVeterinarioRepository(veterinario):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlDeleteRepository = "delete from veterinario where id=%s"
            valor = veterinario
            cursor.execute(sqlDeleteRepository, (valor,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def updateveterinarioRepository(veterinario):
        try:
            con = Conexao.getConnection('')
            cursor = con.cursor()

            sqlUpateVeterinario = "update veterinario set nome=%s, cpf=%s, nascimento=%s, telefone=%s, email=%s, formacao=%s where id=%s"
            cursor.execute(sqlUpateVeterinario, (veterinario.nomeVeterinario, veterinario.cpfVeterinario,
                           veterinario.nascimentoVeterinario, veterinario.telefoneVeterinario, veterinario.emailVeterinario, veterinario.formacao, veterinario.idVeterinario))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()
