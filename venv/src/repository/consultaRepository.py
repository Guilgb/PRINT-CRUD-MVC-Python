from src.config.database import Conexao, psycopg2


class ConsultaRepository:
    def repositoryConsulta(idConsulta, dataConsulta, horarioConsulta, pagamento, observacao, animal, funcionario):

        con = Conexao.getConnection('')
        cursor = con.cursor()

        try:
            def BuscarIdAnimal():
                sqlBuscarAnimal = "SELECT id FROM animal where nome = %s"
                valor = animal
                cursor.execute(sqlBuscarAnimal, (valor,))
                resultadoAnimal = cursor.fetchone()

                for idanimal in resultadoAnimal:
                    return idanimal

            def buscarIdFuncionario():
                sqlBuscarFuncionario = "SELECT id from funcionario where nome= %s"
                valor = funcionario
                cursor.execute(sqlBuscarFuncionario, (valor,))
                resultadoBuscaFuncionario = cursor.fetchone()
                for resultadoIdFuncionario in resultadoBuscaFuncionario:
                    return resultadoIdFuncionario

            animalId = BuscarIdAnimal()
            funcionarioId = buscarIdFuncionario()

            sql = "insert into agendamento (data, horario, observação, funcionarioId) values(%s, %s,%s, %s, %s, %s)"
            valores = (dataConsulta, horarioConsulta, pagamento,
                       observacao, funcionarioId, animalId)
            cursor.execute(sql, valores)
            con.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if con is not None:
                con.close()
