from features.importar_dados.metodos.base_dados import BaseDados


class EstruturaBanco:

    def __init__(self) -> None:
        self.conexao_banco = BaseDados()

    def estrutura_banco(self):
        self.conexao_banco.estabelecer_conexao()
        self.conexao_banco.cria_tabela_resumo_pedido_cliente()
        self.conexao_banco.cria_indices_tabela_resumo_pedido_cliente()
        self.conexao_banco.commitar_alteracoes()
        self.conexao_banco.fechar_conexao()

    def criar_estrutura(self):
        self.estrutura_banco()
