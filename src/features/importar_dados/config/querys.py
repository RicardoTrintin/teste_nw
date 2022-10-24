from utils.decorators import execute_query


@execute_query
def insere_dados_na_tabela(dados):
    return f"""
        {dados}
    """

@execute_query
def cria_tabela_resumo_pedidos_cliente():
    return """
        CREATE TABLE resumo_pedidos_cliente (
            id SERIAL,
            cpf varchar(15),
            cnpj VARCHAR(20),
            private integer,
            incompleto integer,
            data_ultima_compra DATE,
            ticket_medio decimal,
            ticket_ultima_compra decimal,
            loja_frequente VARCHAR(20),
            loja_ultima_compra VARCHAR,
            created_at timestamp,
            updated_at timestamp
        );
    """

@execute_query
def cria_indices_tabela_resumo_pedidos_cliente():
    return """
        CREATE INDEX cpf_index on resumo_pedidos_cliente (cpf);
        CREATE INDEX cnpj_index on resumo_pedidos_cliente (cnpj);
        CREATE INDEX data_ultima_compra_index on resumo_pedidos_cliente (data_ultima_compra);
        CREATE INDEX loja_frequente_index on resumo_pedidos_cliente (loja_frequente);
        CREATE INDEX loja_ultima_compra_index on resumo_pedidos_cliente (loja_ultima_compra);
    """
