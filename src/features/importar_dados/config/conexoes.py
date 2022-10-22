import psycopg2

from settings import DATABASE


class Conexao:

    def connect_base(self):
        try:
            mysql_database = psycopg2.connect(**DATABASE)
            return mysql_database
        except Exception as e:
            raise ConnectionError([e, "ERRO DE CONEXAO COM O BANCO DE DADOS"])

    def open_connection(self):
        return self.connect_base()

    def commit_transacoes(self, conexao):
        return conexao.commit()

    def rollback_transacoes(self, conexao):
        return conexao.rollback()

    def close_connection(self, conexao):
        return conexao.close()