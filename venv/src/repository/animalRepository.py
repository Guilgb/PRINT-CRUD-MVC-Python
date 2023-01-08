from src.config.database import Conexao


class AnimalRepository:
    def repositoryAnimal(nomeAnimal, especie, sexo, raca, peso, nascimento, cliente):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        def buscarIdCliente():
            sqlBuscarCliente = "SELECT id FROM cliente WHERE nome = %s"
            valor = cliente
            cursor.execute(sqlBuscarCliente, (valor,))
            resultadoBusca = cursor.fetchone()

            for resultado in resultadoBusca:
                return resultado

        # resultadoFinal = buscarIdCliente()
        # sql = "insert into animal (nome, especie, sexo, raca, peso, nascimento, clienteId) values(%s, %s, %s, %s, %s, %s, %s);"
        # value = (nomeAnimal, especie, sexo,
        #          raca, peso, nascimento, resultadoFinal)
        # cursor.execute(sql, value)
        # con.commit()
