import os
import pandas as pd

class Evento:

    def __init__(self, diretorio):
        arquivo = open("./Listas/" + diretorio + "/info.txt", "r")
        linhas = arquivo.readlines()
        arquivo.close()
        self.dados = {}
        for linha in linhas:
            linha = linha.split(":")
            linha[0] = linha[0].strip()
            linha[1] = linha[1].rstrip()
            linha[1] = linha[1].lstrip()
            self.dados[linha[0]] = linha[1]
        self.dados["carga"] = int(self.dados["carga"])
        self.lista = pd.read_csv("./Listas/" + diretorio + "/Participantes.csv", encoding="utf-8-sig", sep=";", engine="python")
        self.nomes = list(self.lista["Nome"])
        self.tipos_participantes = list(self.lista["Tipo"])

    def criar_diretorio(self):
        para_criar = "./Certificados/" + self.dados["nome"]
        while(os.path.exists(para_criar)):
            para_criar += "1"
        os.mkdir(para_criar)
        self.diretorio = para_criar




