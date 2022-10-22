from lib2to3.pytree import Base
from metodos.base_dados import BaseDados


class Executar:

    def __init__(self) -> None:
        self.conexao_banco = BaseDados()
        self.caminho_arquivo = 'src\\arquivos\\base_teste.txt'
        self.arquivo_presente = False
        try:
            with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
                self.arquivo_presente = True
            arquivo.close()
        except FileNotFoundError:
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

    def run_script(self):
        if self.arquivo_presente:
            string_insert = "INSERT INTO teste (teste) VALUES"
            with open("src\\arquivos\\base_teste.txt", "r", encoding="utf-8") as arquivo:
                dados_arquivo = arquivo.readlines()

            for index, dado in enumerate(dados_arquivo):
                if index != 0:
                    dado = self.map_campos(dado.split())
                    string_insert += f"""('{dado.get("cpf")}'), """
                    # self.inser_dados_na_base(dado)
                    print("cliente inserido na tabela")
            with open("src\\arquivos\\inserts.txt", "a") as arquivo:
                arquivo.write(string_insert)
                teste = arquivo.read()
                # self.inser_dados_na_base(dado)
            print("Importação finalizada com sucesso")
