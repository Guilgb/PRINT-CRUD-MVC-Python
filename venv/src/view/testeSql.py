from src.config.database import Conexao

con = Conexao.getConnection('')
cursor = con.cursor()


def ok():
    sqlBuscarCliente = "SELECT id FROM cliente WHERE nome = %s"
    valor = "Guilherme"
    cursor.execute(sqlBuscarCliente, (valor,))
    resultadoBusca = cursor.fetchone()

    for resultado in resultadoBusca:
        return resultado
