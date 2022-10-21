# import unidecode
from utils.decorators import loop_rotina
from utils.util import Util
from execucao_script import Executar


@loop_rotina()
def executar_rotina():
    Executar().run_script()


if __name__ == '__main__':
    executar_rotina()
