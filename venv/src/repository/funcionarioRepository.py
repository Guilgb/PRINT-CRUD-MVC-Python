from src.config.database import Conexao


class FuncionarioRepository:
    def insertFuncionario(idFuncionario, nomeFuncionario, nascimentoFuncionario, emailFuncionario, telefoneFuncionario, cargo):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        sql = "insert into funcionario (nome, nascimento, email, telefone, cargo) values(%s, %s, %s, %s, %s)"
        valores = (nomeFuncionario, nascimentoFuncionario,
                   emailFuncionario, telefoneFuncionario, cargo)

        cursor.execute(sql, valores)
        con.commit()
