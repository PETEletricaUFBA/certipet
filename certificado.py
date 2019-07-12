from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import funcoes_auxiliares as func
import template



class Certificado:

    def __init__(self, evento):
        self.dados_template = template.Template(evento.dados["modelo"])
        fontes = self.dados_template.retornar_fontes()
        pdfmetrics.registerFont(TTFont("Nome", fontes[0]))
        pdfmetrics.registerFont(TTFont("Texto", fontes[1]))
        self.evento = evento

    def gerar(self):
        #Constantes de Posicionamento
        k1,k2,k3,k4,k5,k6 = self.dados_template.retornar_constantes()

        #Textos

        textos1 = self.dados_template.retornar_texto1()
        tipo = self.evento.dados["tipo"]
        pre2 = "de" if tipo == "minicurso" else "sobre"
        nome_evento = self.evento.dados["nome"]
        data = "em " + self.evento.dados["data"]

        for i in range(0, len(self.evento.nomes)):
            nome = self.evento.nomes[i]
            nome = nome.lower()
            nome = nome.title()
            tipo_participante = self.evento.tipos_participantes[i]

            inicio = "Participou" if tipo_participante == 0 else "Ministrou"
            carga = "na Universidade Federal do Tocantins com carga horária de "
            pre1 = ""
            if(tipo_participante == 0):
                carga += str(self.evento.dados["carga"]) + " horas."
            else:
                carga += str(self.evento.dados["carga"] * 2) + " horas."

            if(tipo == "minicurso"):
                if(tipo_participante == 0):
                    pre1 = "do"
                else:
                    pre1 = "o"

            else:
                if(tipo_participante == 0):
                    pre1 = "da"
                else:
                    pre1 = "a"

            texto_intermediario = inicio + " " + pre1 + " " + tipo + " " + pre2 + " " + nome_evento + " " + data + " " + carga
            texto2 = func.dividir_linhas(texto_intermediario, k3)

            arquido_pdf = self.evento.diretorio + "/" + nome + ".pdf"
            cnv = canvas.Canvas(arquido_pdf, pagesize=landscape(A4))
            fundo = self.dados_template.retornar_fundo()
            cnv.drawImage("./template/" + fundo, width=A4[1], height=A4[0], x=0, y=0)

            #Desenho
            tamanho1, tamanho2 = self.dados_template.retornar_tamanho_fontes()
            cor1, cor2 = self.dados_template.retornar_cores()
            pos_header, pos_nome, pos_bottom = self.dados_template.retornar_posicoes()

            # Header Text
            cnv.setFont("Texto", tamanho1, leading=None)
            cnv.setFillColorRGB(cor1[0], cor1[1], cor1[2])
            for i in range(0, len(textos1)):
                texto1 = textos1[i]
                cnv.drawString(pos_header[0] - k5 * len(texto1), pos_header[1] - i*k6, texto1)

            # Nome
            cnv.setFont("Nome", tamanho2, leading=None)
            cnv.setFillColorRGB(cor2[0], cor2[1], cor2[2])
            pos_x = pos_nome[0] - k1 * len(nome)
            pos_y = pos_nome[1]
            cnv.drawString(pos_x, pos_y, nome)

            # Bottom Text
            cnv.setFont("Texto", tamanho1, leading=None)
            cnv.setFillColorRGB(cor1[0], cor1[1], cor1[2])
            pos_x_base = pos_bottom[0]
            pos_y_base = pos_bottom[1]
            for i in range(0, len(texto2)):
                cnv.drawString(pos_x_base - k2*len(texto2[i]), pos_y_base - i*k4, texto2[i])
            cnv.save()

