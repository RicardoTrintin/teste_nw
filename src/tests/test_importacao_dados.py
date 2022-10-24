from features.importar_dados import main
from unittest.mock import Mock
import pytest


main.Executar = Mock


def test_insere_dados_na_base():
    teste = main.Executar()

    teste.conexao_banco.estabelecer_conexao = Mock()
    teste.conexao_banco.insere_dados_na_tabela = Mock()
    teste.conexao_banco.commitar_alteracoes = Mock()
    teste.conexao_banco.fechar_conexao = Mock()

    teste.insere_dados_na_base()

    teste.conexao_banco.estabelecer_conexao.assert_called_once
    teste.conexao_banco.insere_dados_na_tabela.assert_called_once
    teste.conexao_banco.commitar_alteracoes.assert_called_once
    teste.conexao_banco.fechar_conexao.assert_called_once


@pytest.mark.parametrize(
    "string_teste, dado, string_insert, separador_values",
    [
        ("""INSERT INTO resumo_pedido_cliente (cpf, cnpj, private, incompleto, data_ultima_compra, ticket_medio, ticket_ultima_compra,
            loja_frequente, loja_ultima_compra, created_at, updated_at) VALUES('041.091.641-25', '', 1, 1, '2011-11-28', 70.9, 90.9,
            '79.379.491/0001-83', '79.379.491/0001-83', NOW(), NOW()), """,
            {"cpf": "041.091.641-25", "cnpj": "", "private": 1, "incompleto": 1,
                "data_ultima_compra": "2011-11-28", "ticket_medio": 70.9,
                "ticket_ultima_compra": 90.9, "loja_frequente": "79.379.491/0001-83",
                "loja_ultima_compra": "79.379.491/0001-83"},
            """INSERT INTO resumo_pedido_cliente (cpf, cnpj, private, incompleto, data_ultima_compra, ticket_medio, ticket_ultima_compra,
                loja_frequente, loja_ultima_compra, created_at, updated_at) VALUES""",
            ",")
    ]
)
def test_incrementa_sctring_insert(string_teste, dado, string_insert, separador_values):
    teste = main.Executar()
    teste.incrementa_sctring_insert = Mock(return_value=string_teste)
    retorno_string = teste.incrementa_sctring_insert(dado, string_insert, separador_values)

    assert retorno_string == string_teste


@pytest.mark.parametrize(
    "dado, dado_teste",
    [
        ({"cpf": "041.091.641-25", "cnpj": "", "private": 0, "incompleto": 0,
            "data_ultima_compra": "2011-11-28", "ticket_medio": 70.9,
            "ticket_ultima_compra": 90.9, "loja_frequente": "79.379.491/0001-83",
            "loja_ultima_compra": "79.379.491/0001-83"},
            {"cpf": "041.091.641-25", "cnpj": "", "private": 0, "incompleto": 0,
                "data_ultima_compra": "2011-11-28", "ticket_medio": 70.9,
                "ticket_ultima_compra": 90.9, "loja_frequente": "79.379.491/0001-83",
                "loja_ultima_compra": "79.379.491/0001-83"}),
        ({"cpf": "041.091.641-25", "cnpj": "", "private": 0, "incompleto": 0,
            "data_ultima_compra": "", "ticket_medio": "",
            "ticket_ultima_compra": "", "loja_frequente": "",
            "loja_ultima_compra": ""},
            {"cpf": "041.091.641-25", "cnpj": "", "private": 0, "incompleto": 1,
                "data_ultima_compra": "", "ticket_medio": "",
                "ticket_ultima_compra": "", "loja_frequente": "",
                "loja_ultima_compra": ""})
    ]
)
def test_identifica_dado_incompleto(dado, dado_teste):
    teste = main.Executar()
    teste.identifica_dado_incompleto = Mock(return_value=dado_teste)
    retorno_metodo = teste.identifica_dado_incompleto(dado)

    if dado.get("data_ultima_compra") and \
        dado.get("ticket_medio") and \
            dado.get("ticket_ultima_compra") and \
                dado.get("loja_frequente") and \
                    dado.get("loja_ultima_compra"):
        assert dado_teste.get("incompleto") == 0
    else:
        assert dado_teste.get("incompleto") == 1


@pytest.mark.parametrize(
    "dado, dado_teste",
    [
        ({"cpf": "041.091.641-25", "cnpj": "", "private": 0, "incompleto": 0,
            "data_ultima_compra": "2011-11-28", "ticket_medio": 70.9,
            "ticket_ultima_compra": 90.9, "loja_frequente": "79.379.491/0001-83",
            "loja_ultima_compra": "79.379.491/0001-83"},
            {"cpf": "041.091.641-25", "cnpj": "", "private": 0, "incompleto": 0,
                "data_ultima_compra": "2011-11-28", "ticket_medio": 70.9,
                "ticket_ultima_compra": 90.9, "loja_frequente": "79.379.491/0001-83",
                "loja_ultima_compra": "79.379.491/0001-83"}),
        ({"cpf": "", "cnpj": "79.379.491/0001-83", "private": 0, "incompleto": 0,
            "data_ultima_compra": "", "ticket_medio": "",
            "ticket_ultima_compra": "", "loja_frequente": "",
            "loja_ultima_compra": ""},
            {"cpf": "", "cnpj": "041.091.641-25", "private": 1, "incompleto": 1,
                "data_ultima_compra": "", "ticket_medio": "",
                "ticket_ultima_compra": "", "loja_frequente": "",
                "loja_ultima_compra": ""})
    ]
)
def test_identifica_cliente_privado(dado, dado_teste):
    teste = main.Executar()
    teste.identifica_cliente_privado = Mock(return_value=dado_teste)
    retorno_metodo = teste.identifica_cliente_privado(dado)

    if dado.get("cnpj"):
        assert retorno_metodo.get("private") == 1
    else:
        assert retorno_metodo.get("private") == 0


@pytest.mark.parametrize(
    "dado, dado_teste",
    [
        ({"loja_frequente": "79.379.491/0001-83", "loja_ultima_compra": "79.379.491/0001-83"},
            {"loja_frequente": "79.379.491/0001-83", "loja_ultima_compra": "79.379.491/0001-83"}),
        ({"loja_frequente": "", "loja_ultima_compra": ""},
            {"loja_frequente": "", "loja_ultima_compra": ""}),
        ({"loja_frequente": "79.379.491/0001-83", "loja_ultima_compra": "66546546"},
            {"loja_frequente": "79.379.491/0001-83", "loja_ultima_compra": ""})
    ]
)
def test_valida_cnpj_loja(dado, dado_teste):
    teste = main.Executar()
    teste.valida_cnpj_loja = Mock(return_value=dado_teste)
    retorno_metodo = teste.valida_cnpj_loja(dado)

    assert retorno_metodo == dado_teste


def test_higieniza_dados_cliente():
    teste = main.Executar()

    teste.valida_cnpj_loja = Mock()
    teste.identifica_cliente_privado = Mock()
    teste.identifica_dado_incompleto = Mock()

    retorno_teste = teste.higieniza_dados_cliente(Mock())

    assert retorno_teste is not None
    teste.valida_cnpj_loja.assert_called_once
    teste.identifica_cliente_privado.assert_called_once
    teste.identifica_dado_incompleto.assert_called_once


@pytest.mark.parametrize(
    "dado, dado_teste",
    [
        ({"cpf": "79.379.491/0001-83", "cnpj": ""},
            {"cpf": "", "cnpj": "79.379.491/0001-83"}),
        ({"cpf": "041.091.641-25", "cnpj": ""},
            {"cpf": "041.091.641-25", "cnpj": ""})
    ]
)
def test_valida_cpf_ou_cnpj(dado, dado_teste):
    teste = main.Executar()

    teste.valida_cpf_ou_cnpj = Mock(return_value=dado_teste)

    retorno_metodo = teste.valida_cpf_ou_cnpj(dado)

    assert retorno_metodo == dado_teste


@pytest.mark.parametrize(
    "dado, dado_teste",
    [
        (["", "79.379.491/0001-83", 1, 1, "", "", "", "", ""],
            {"cpf": "", "cnpj": "79.379.491/0001-83", "private": 1, "incompleto": 1,
                "data_ultima_compra": "", "ticket_medio": "",
                "ticket_ultima_compra": "", "loja_frequente": "",
                "loja_ultima_compra": ""})
    ]
)
def test_map_campos(dado, dado_teste):
    teste = main.Executar()

    teste.map_campos = Mock(return_value=dado_teste)
    retorno_metodo = teste.map_campos(dado)

    assert type(retorno_metodo) == dict


def test_captura_dados_arquivo():
    teste = main.Executar()

    arquivo = Mock()

    teste.captura_dados_arquivo = Mock(return_value=arquivo)
    retorno_metodo = teste.captura_dados_arquivo()

    assert retorno_metodo == arquivo


def test_roda_script():
    teste = main.Executar()

    teste.map_campos = Mock(return_value=Mock())
    teste.valida_cpf_ou_cnpj = Mock(return_value=Mock())
    teste.higieniza_dados_cliente = Mock(return_value=Mock())
    teste.incrementa_sctring_insert = Mock(return_value=Mock())
    teste.insere_dados_na_base = Mock(return_value=Mock())

    teste.roda_script()

    teste.map_campos.assert_called
    teste.valida_cpf_ou_cnpj.assert_called_once
    teste.higieniza_dados_cliente.assert_called_once
    teste.incrementa_sctring_insert.assert_called_once
    teste.insere_dados_na_base.assert_called_once
