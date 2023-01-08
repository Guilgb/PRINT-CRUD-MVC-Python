import psycopg2


class Conexao:
    def __init__(self):
        pass

    def getConnection(self):
        con = psycopg2.connect(
            host='localhost',
            port='5432',
            database='PRINT',
            user='postgres',
            password=1234
        )
        return con
