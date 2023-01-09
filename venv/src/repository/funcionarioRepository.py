from src.config.database import Conexao, psycopg2


class FuncionarioRepository:
    def insertFuncionario(idFuncionario, nomeFuncionario, nascimentoFuncionario, emailFuncionario, telefoneFuncionario, cargo):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sql = "insert into funcionario (nome, nascimento, email, telefone, cargo) values(%s, %s, %s, %s, %s)"
            valores = (nomeFuncionario, nascimentoFuncionario,
                       emailFuncionario, telefoneFuncionario, cargo)

            cursor.execute(sql, valores)
            con.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
