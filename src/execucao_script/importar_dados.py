import shutil
from metodos.base_dados import BaseDados
import os


class Executar:

    def __init__(self) -> None:
        self.conexao_banco = BaseDados()
        self.caminho_arquivo = 'src\\arquivos\\base_teste.txt'
        if not os.path.exists("src\\arquivos\\arquivo_para_importar\\base_teste.txt"):
            raise FileNotFoundError(
                "Arquivo não encontrado, como entrada, é necessário estar dentro da pasta src/arquivos e com o nome base_teste")

    def inser_dados_na_base(self, dados):
        self.conexao_banco.estabelecer_conexao()
        self.conexao_banco.insere_dados_na_tabela(dados)
        self.conexao_banco.commitar_alteracoes()
        self.conexao_banco.fechar_conexao()

    def map_campos(self, dado):
        dado_mapeado = {
            "cpf": dado[0],
            "private": dado[1],
            "incompleto": dado[2],
            "data_ultima_compra": dado[3],
            "ticket_medio": dado[4],
            "ticket_ultima_compra": dado[5],
            "loja_frequente": dado[6],
            "loja_ultima_compra": dado[7]
        }
        return dado_mapeado

    def captura_dados_arquivo(self):
        with open("src\\arquivos\\arquivo_para_importar\\base_teste.txt", "r", encoding="utf-8") as arquivo:
            dados_arquivo = arquivo.readlines()
        arquivo.close()
        return dados_arquivo

    def move_arquivo_para_importados(self):
        shutil.move("src\\arquivos\\arquivo_para_importar\\base_teste.txt", "src\\arquivos\\arquivos_importados\\base_teste.txt")

    def run_script(self):
        string_insert = "INSERT INTO teste (teste) VALUES"
        dados_arquivo = self.captura_dados_arquivo()
        for index, dado in enumerate(dados_arquivo):
            if index != 0:
                dado = self.map_campos(dado.split())
                if index == (len(dados_arquivo) - 1):
                    string_insert += f"""('{dado.get("cpf")}');"""
                else:
                    string_insert += f"""('{dado.get("cpf")}'), """
        self.inser_dados_na_base(string_insert)
        self.move_arquivo_para_importados()
        print("Importação dos dados do arquivo finalizada com sucesso")
