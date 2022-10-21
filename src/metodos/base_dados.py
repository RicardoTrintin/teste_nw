from metodos.conexao_abc import ConexaoABC
from config import querys


class BaseDados(ConexaoABC):

    def insere_dados_na_tabela(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.teste(cursor, *args, **kwargs)
