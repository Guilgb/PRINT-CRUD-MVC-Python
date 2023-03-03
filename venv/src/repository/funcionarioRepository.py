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

    def readFuncionarioRepository(self):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlReadRepository = "select * from funcionario"
            cursor.execute(sqlReadRepository)
            readFuncionario = cursor.fetchall()
            return readFuncionario

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

        finally:
            if con is not None:
                con.close()

    def deleteFuncionarioRepository(funcionario):
        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            sqlDeleteFuncionario = "delete from funcionario where id=%s"
            valor = funcionario
            cursor.execute(sqlDeleteFuncionario, (valor,))
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()

    def updateFuncionarioRepository(funcionario):
        pass
