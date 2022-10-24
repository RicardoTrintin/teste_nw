from features.importar_dados.metodos import conexao_abc
from unittest.mock import Mock


conexao_abc.ConexaoABC = Mock()


def test_estabelecer_conexao():
    teste = conexao_abc.ConexaoABC()

    teste.conexao.open_connection = Mock()
    teste.estabelecer_conexao = Mock(return_value=Mock())
    teste.estabelecer_conexao()

    teste.conexao.open_connection.assert_called_once


def test_fechar_conexao():
    teste = conexao_abc.ConexaoABC()

    teste.conexao.close_connection = Mock()
    teste.fechar_conexao = Mock(return_value=Mock())
    teste.fechar_conexao()

    teste.conexao.close_connection.assert_called_once


def test_commitar_alteracoes():
    teste = conexao_abc.ConexaoABC()

    teste.conexao.commit_transacoes = Mock()
    teste.commitar_alteracoes = Mock(return_value=Mock())
    teste.commitar_alteracoes()

    teste.conexao.commit_transacoes.assert_called_once
