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
