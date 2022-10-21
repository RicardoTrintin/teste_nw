import imp
import os

tipo_execucao = os.environ.get('PARAMETRO_EXECUCAO', None)

if tipo_execucao == "CONTROLA_EXEUCAO_HIGIENIZACAO":
    from .hienizar_dados import Executar
elif tipo_execucao == "CONTROLA_EXEUCAO_IMPORTACAO_DADOS":
    from .importar_dados import Executar
