import unidecode
from utils.util import Util

class Main:

    def __init__(self) -> None:
        pass

    def map_campos(self, dado) -> list:
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
        with open("src\\data\\base_teste.txt", "r", encoding="utf-8") as arquivo:
            dados_arquivo = arquivo.readlines()

        for index, dado in enumerate(dados_arquivo):
            if index != 0:
                dado = self.map_campos(dado.split())

app = Main()

app.run_script()