from features.importar_dados.metodos.conexao_abc import ConexaoABC
from features.importar_dados.config import querys


class BaseDados(ConexaoABC):

    def insere_dados_na_tabela(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.insere_dados_na_tabela(cursor, *args, **kwargs)

    def limpa_dado_tabela(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.limpa_dado_tabela(cursor, *args, **kwargs)

    def create_table_resumo_pedidos_cliente(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.create_table_resumo_pedidos_cliente(cursor, *args, **kwargs)

    def create_indices_table_resumo_pedidos_cliente(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.create_indices_table_resumo_pedidos_cliente(cursor, *args, **kwargs)
