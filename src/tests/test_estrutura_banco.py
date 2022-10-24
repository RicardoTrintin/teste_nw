from features.importar_dados.estrutura_banco import estrutura_banco
from unittest.mock import Mock


estrutura_banco.EstruturaBanco = Mock


def test_estrutura_banco():
    teste = estrutura_banco.EstruturaBanco()

    teste.conexao_banco.estabelecer_conexao = Mock()
    teste.conexao_banco.cria_tabela_resumo_pedido_cliente = Mock()
    teste.conexao_banco.cria_indices_tabela_resumo_pedido_cliente = Mock()

    teste.estrutura_banco()

    teste.conexao_banco.estabelecer_conexao.assert_called_once
    teste.conexao_banco.cria_tabela_resumo_pedido_cliente.assert_called_once
    teste.conexao_banco.cria_indices_tabela_resumo_pedido_cliente.assert_called_once


def test_criar_estrutura():
    teste = estrutura_banco.EstruturaBanco()

    teste.estrutura_banco = Mock()

    teste.criar_estrutura()

    teste.estrutura_banco.assert_called_once
