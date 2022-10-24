from features.importar_dados.config import conexoes
from unittest.mock import Mock
import pytest


conexoes.psycopg2 = Mock()


def test_connect_postgres():
    conexao = conexoes.Conexao()

    conn = conexao.connect_base()
    assert conn is not None


def test_connect_postgres_lancando_excecao():
    conexao = conexoes.Conexao()
    conexoes.psycopg2.connect = Mock(side_effect=Exception('Test'))
    with pytest.raises(ConnectionError):
        conexao.connect_base()

    conexoes.psycopg2.connect = Mock()


def test_open_connection_postgres():
    conexao = conexoes.Conexao()
    conn = conexao.open_connection()
    assert conn is not None


def test_commit_transacoes():
    conexao = conexoes.Conexao()
    mock = Mock()
    conn = conexao.commit_transacoes(mock)
    mock.commit.assert_called_once()
    assert conn is not None


def test_close_connection():
    conexao = conexoes.Conexao()
    mock = Mock()
    conn = conexao.close_connection(mock)
    mock.close.assert_called_once()
    assert conn is not None
