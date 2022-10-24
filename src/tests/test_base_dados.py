from features.importar_dados.metodos import base_dados
from features.importar_dados.config import querys
from unittest.mock import Mock


base_dados.BaseDados = Mock


def test_insere_dados_na_tabela():
    teste = base_dados.BaseDados()

    teste.banco_integracao.cursor = Mock()
    teste.insere_dados_na_tabela = Mock()
    querys.insere_dados_na_tabela = Mock()

    teste.insere_dados_na_tabela()

    teste.banco_integracao.cursor.assert_called_once
    querys.insere_dados_na_tabela.assert_called_once


def test_cria_tabela_resumo_pedido_cliente():
    teste = base_dados.BaseDados()

    teste.banco_integracao.cursor = Mock()
    teste.cria_tabela_resumo_pedido_cliente = Mock()
    querys.cria_tabela_resumo_pedido_cliente = Mock()

    teste.cria_tabela_resumo_pedido_cliente()

    teste.banco_integracao.cursor.assert_called_once
    querys.cria_tabela_resumo_pedido_cliente.assert_called_once


def test_cria_indices_tabela_resumo_pedido_cliente():
    teste = base_dados.BaseDados()

    teste.banco_integracao.cursor = Mock()
    teste.cria_indices_tabela_resumo_pedido_cliente = Mock()
    querys.cria_indices_tabela_resumo_pedido_cliente = Mock()

    teste.cria_indices_tabela_resumo_pedido_cliente()

    teste.banco_integracao.cursor.assert_called_once
    querys.cria_indices_tabela_resumo_pedido_cliente.assert_called_once
