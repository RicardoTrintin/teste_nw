from features.importar_dados.config.conexoes import Conexao
from abc import ABC
import psycopg2


class ConexaoABC(ABC):

    def __init__(self):
        self.conexao = Conexao()
        self.banco_integracao = psycopg2.connect

    def estabelecer_conexao(self):
        self.banco_integracao = self.conexao.open_connection()

    def fechar_conexao(self):
        self.conexao.close_connection(self.banco_integracao)

    def commitar_alteracoes(self):
        self.conexao.commit_transacoes(self.banco_integracao)

    def rollback(self):
        self.conexao.rollback_transacoes(self.banco_integracao)
