import psycopg2


class Conexao:
    def __init__(self):
        pass

    def getConnection(self):
        con = psycopg2.connect(
            host='localhost',
            database='PRINT-DB',
            user='postgres',
            password=1234
        )
        return con
