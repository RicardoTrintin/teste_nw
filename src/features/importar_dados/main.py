from features.importar_dados.metodos.base_dados import BaseDados
from validate_docbr import CPF, CNPJ
import shutil
import os


class Executar:

    def __init__(self) -> None:
        self.conexao_banco = BaseDados()
        self.cpf = CPF()
        self.cnpj = CNPJ()
        self.caminho_arquivo_base = os.environ.get("CAMINHO_ARQUIVO", "features/importar_dados/arquivos/base_teste.txt")
        self.caminho_arquivo_base = "features/importar_dados/arquivos/base_teste.txt"
        # self.caminho_arquivo_importados = os.environ.get("CAMINHO_ARQUIVO_IMPORTADOS_BASE", "CAMINHO_ARQUIVO_IMPORTADOS_DEFAULT")
        # self.caminho_arquivo_importados = "features/importar_dados/arquivos/arquivos_importados/base_teste.txt"
        if not os.path.exists(self.caminho_arquivo_base):
            raise FileNotFoundError(
                f"Arquivo não encontrado no caminho, como entrada, nas pastas default ou no caminho especificado pelo usuario")

    # def move_arquivo_para_importados(self):
    #     shutil.move(self.caminho_arquivo_base, self.caminho_arquivo_importados)

    def insere_dados_na_base(self, dados):
        self.conexao_banco.estabelecer_conexao()
        self.conexao_banco.insere_dados_na_tabela(dados)
        self.conexao_banco.commitar_alteracoes()
        self.conexao_banco.fechar_conexao()

    def incrementa_sctring_insert(self, dado, string_insert, separador_values):
        string_insert += f"""('{dado.get("cpf")}', '{dado.get("cnpj")}', {dado.get("private")},
                {dado.get("incompleto")}, '{dado.get("data_ultima_compra")}', {dado.get("ticket_medio")},
                {dado.get("ticket_ultima_compra")}, '{dado.get("loja_frequente")}', '{dado.get("loja_ultima_compra")}',
                NOW(), NOW()){separador_values} """
        return string_insert

    def identifica_dado_incompleto(self, dado):
        valida_incompleto = True
        # identifica dados incompletos do cliente
        if dado.get("data_ultima_compra") and \
            dado.get("ticket_medio") and \
                dado.get("ticket_ultima_compra") and \
                    dado.get("loja_frequente") and \
                        dado.get("loja_ultima_compra"):
                valida_incompleto = False
        if valida_incompleto:
            dado['incompleto'] = 1
        return dado

    def identifica_cliente_privado(self, dado):
        # valida cnpj para identificar cliente juridico
        if dado.get("cnpj"):
            dado["private"] = 1
        else:
            dado["private"] = 0
        return dado

    def valida_cnpj_loja(self, dado):
        if dado.get("loja_frequente") and dado.get("loja_ultima_compra"):
            if not self.cnpj.validate(dado.get("loja_frequente")):
                dado['loja_frequente'] = ''
            if not self.cnpj.validate("loja_ultima_compra"):
                dado['loja_ultima_compra'] = ''
        return dado

    def higieniza_dados_cliente(self, dado):
        dado = self.valida_cnpj_loja(dado)
        dado = self.identifica_cliente_privado(dado)
        dado = self.identifica_dado_incompleto(dado)
        return dado

    def valida_cpf_ou_cnpj(self, dado):
        identificador_cliente_valido = True
        cpf_valido = self.cpf.validate(dado.get("cpf"))
        if not cpf_valido:
            cnpj_valido = self.cnpj.validate(dado.get("cpf"))
            if not cnpj_valido:
                identificador_cliente_valido = False
            else:
                dado['cnpj'] = dado.get('cpf')
            dado['cpf'] = ''
        return identificador_cliente_valido, dado

    def map_campos(self, dado):
        dado_mapeado = {
            "cpf": dado[0] if dado[0] else '',
            "cnpj": "",
            "private": dado[1] if dado[1] != 'NULL' else '',
            "incompleto": dado[2] if dado[2] != 'NULL' else '',
            "data_ultima_compra": str(dado[3]) if dado[3] != 'NULL' else None,
            "ticket_medio": dado[4].replace(",", ".") if dado[4] != 'NULL' else 0,
            "ticket_ultima_compra": dado[5].replace(",", ".") if dado[5] != 'NULL' else 0,
            "loja_frequente": dado[6] if dado[6] != 'NULL' else '',
            "loja_ultima_compra": dado[7] if dado[7] != 'NULL' else '',
        }
        return dado_mapeado

    def limpa_dado_tabela(self):
        self.conexao_banco.estabelecer_conexao()
        self.conexao_banco.limpa_dado_tabela()
        self.conexao_banco.commitar_alteracoes()
        self.conexao_banco.fechar_conexao()

    def captura_dados_arquivo(self):
        with open(self.caminho_arquivo_base, "r", encoding="utf-8") as arquivo:
            dados_arquivo = arquivo.readlines()
        arquivo.close()
        return dados_arquivo

    def run_script(self):
        string_insert = """INSERT INTO resumo_pedidos_cliente (cpf, cnpj, private, incompleto, data_ultima_compra, ticket_medio,
            ticket_ultima_compra, loja_frequente, loja_ultima_compra, created_at, updated_at) VALUES"""
        dados_arquivo = self.captura_dados_arquivo()
        self.limpa_dado_tabela()
        separador_values = ","

        for index, dado in enumerate(dados_arquivo):
            if index != 0:
                dado = self.map_campos(dado.split())
                identificador_cliente_valido, dado = self.valida_cpf_ou_cnpj(dado)
                if identificador_cliente_valido:
                    dado = self.higieniza_dados_cliente(dado)
                    if index == (len(dados_arquivo) - 1):
                        separador_values = ";"
                    string_insert = self.incrementa_sctring_insert(dado, string_insert, separador_values)
                else:
                    print(f"cpf ou cnpj não é valido: {dado.get('cpf')}")

        self.insere_dados_na_base(string_insert)
        # self.move_arquivo_para_importados()
        print("Importação dos dados do arquivo finalizada com sucesso")
