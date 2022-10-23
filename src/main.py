# import unidecode
from features.importar_dados.main import Executar
from utils.exceptions import ImportDataException, QueryException, VariableAmbienteException


def executar_rotina():
    try:
        Executar().run_script()
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


if __name__ == '__main__':
    executar_rotina()
