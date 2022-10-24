from utils.exceptions import QueryException


def execute_query(f):
    def execute(cursor, *args, **kwargs):
        try:
            cursor.execute(f(*args, **kwargs).replace("'None'", 'Null'))
            return cursor
        except ConnectionError as e:
            raise QueryException(e)
        except Exception as e:
            raise QueryException(e)

    return execute


def busca_um_item_query(f):
    def busca_um_item(cursor, *args, **kwargs):
        try:
            cursor.execute(f(*args, **kwargs).replace("'None'", 'Null'))
            item = cursor.fetchone()
            if item and len(item) > 0:
                return dict(zip([desc[0] for desc in cursor.description], item))
            else:
                return item
        except ConnectionError as e:
            raise QueryException(e)
        except Exception as e:
            raise QueryException(e)

    return busca_um_item


def busca_todos_itens_query(f):
    def busca_todos_itens(cursor, *args, **kwargs):
        try:
            cursor.execute(f(*args, **kwargs).replace("'None'", 'Null'))
            todos_itens = cursor.fetchall()
            if len(todos_itens) > 0:
                return [dict(zip([desc[0] for desc in cursor.description], row)) for row in todos_itens]
            else:
                return todos_itens
        except ConnectionError as e:
            e, extra = e.args[0]
            raise QueryException(e)
        except Exception as e:
            raise QueryException(e)

    return busca_todos_itens
