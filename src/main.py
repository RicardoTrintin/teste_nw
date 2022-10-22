# import unidecode
from utils.decorators import loop_rotina
import os

tipo_execucao = os.environ.get('PARAMETRO_EXECUCAO', None)

if tipo_execucao == "CONTROLA_EXEUCAO_HIGIENIZACAO":
    from features.higienizar_dados.main import Executar
elif tipo_execucao == "CONTROLA_EXEUCAO_IMPORTACAO_DADOS":
    from features.importar_dados.main import Executar


@loop_rotina()
def executar_rotina():
    Executar().run_script()


if __name__ == '__main__':
    executar_rotina()
