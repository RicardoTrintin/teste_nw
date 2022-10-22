from utils.decorators import execute_query, busca_todos_itens_query, busca_um_item_query


@execute_query
def teste(dados):
    return f"""
        {dados}
    """


@execute_query
def limpa_dado_tabela():
    return f"""
        DELETE FROM teste
    """
