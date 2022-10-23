from features.importar_dados.metodos.base_dados import BaseDados


class EstruturaBanco:

    def __init__(self) -> None:
        self.conexao_banco = BaseDados()

    def estrutura_banco(self):
        self.conexao_banco.estabelecer_conexao()
        self.conexao_banco.create_table_resumo_pedidos_cliente()
        self.conexao_banco.create_indices_table_resumo_pedidos_cliente()
        self.conexao_banco.commitar_alteracoes()
        self.conexao_banco.fechar_conexao()

    def criar_estrutura(self):
        self.estrutura_banco()
