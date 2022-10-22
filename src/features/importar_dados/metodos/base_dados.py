from features.importar_dados.metodos.conexao_abc import ConexaoABC
from features.importar_dados.config import querys


class BaseDados(ConexaoABC):

    def insere_dados_na_tabela(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.teste(cursor, *args, **kwargs)

    def limpa_dado_tabela(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.limpa_dado_tabela(cursor, *args, **kwargs)
