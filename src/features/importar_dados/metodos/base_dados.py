from features.importar_dados.metodos.conexao_abc import ConexaoABC
from features.importar_dados.config import querys


class BaseDados(ConexaoABC):

    def insere_dados_na_tabela(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.insere_dados_na_tabela(cursor, *args, **kwargs)

    def cria_tabela_resumo_pedido_cliente(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.cria_tabela_resumo_pedido_cliente(cursor, *args, **kwargs)

    def cria_indices_tabela_resumo_pedido_cliente(self, *args, **kwargs):
        with self.banco_integracao.cursor() as cursor:
            return querys.cria_indices_tabela_resumo_pedido_cliente(cursor, *args, **kwargs)
