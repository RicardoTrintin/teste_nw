from utils.exceptions import ImportDataException, QueryException, VariableAmbienteException
import schedule
import time
import os


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


def loop_rotina():
    def decorator(func):
        try:
            if not os.environ.get("PARAMETRO_EXECUCAO") or not os.environ.get("TEMPO_ROTINA") or not os.environ.get("SLEEP_ROTINA"):
                raise VariableAmbienteException("VARIÁVEIS DE AMBIENTE NAO CONFIGURADAS")
            else:
                schedule.every(int(os.environ.get('TEMPO_ROTINA'))).minutes.do(func)

                while True:
                    schedule.run_pending()
                    time.sleep(int(os.environ.get('SLEEP_ROTINA')))

        except ImportDataException as e:
            raise ImportDataException(e)
        except QueryException as e:
            raise QueryException(e)
        except ConnectionError as e:
            raise ConnectionError(e)
        except FileNotFoundError as e:
            raise FileNotFoundError(e)
        except VariableAmbienteException as e:
            raise VariableAmbienteException(e)
        except Exception as e:
            raise Exception(e)

    return decorator
