class ImportDataException(Exception):
    """É lancada quando ocorre algum erro de importação e se tem os dados de impressão"""
    pass


class QueryException(Exception):
    """É lancada quando ocorre algum erro na execução de uma query"""
    pass


class VariableAmbienteException(Exception):
    """É lançada quando as variaveis de ambiente no yml ou localmente não está configuradas"""
    pass
