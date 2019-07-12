from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph, Spacer
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm


pdfmetrics.registerFont(TTFont("Lucida", "Lucida Bright.ttf"))
pdfmetrics.registerFont(TTFont("Bank", "BankGothic Md BT Medium.ttf"))


cnv = canvas.Canvas("teste.pdf", pagesize=landscape(A4))

cnv.drawImage("./template/fundo.png", width=A4[1], height=A4[0], x = 0, y = 0)

#Header Text
cnv.setFont("Bank", 20, leading=None)
cnv.setFillColorRGB(0.3, 0.3, 0.3)
texto1 = "O PET Engenharia Elétrica UFT declara que"
cnv.drawString(170, 340, texto1)

#Nome
cnv.setFont("Lucida", 30, leading=None)
cnv.setFillColorRGB(0, 0.8, 0.8)
nome = "Cícero Matheus da Silva Lacerda"
pos_x = 420 - 7.5*len(nome)
pos_y = 280
cnv.drawString(pos_x, pos_y, nome)


#Bottom Text
cnv.setFont("Bank", 20, leading=None)
cnv.setFillColorRGB(0.3, 0.3, 0.3)

inicio = "Participou"
prep = "do"
tipo = "minicurso"
nome = "Luminotécnica".upper()
prep2 = "em"
data = "08 de Setembro de 2018"
resto = "na Universidade Federal do Tocantins"
prep3 = "com carga horária total de"
carga = "8 (oito) horas."

texto = inicio + " " + prep + " " + tipo + " " + nome + " " + prep2 + " " + data + " " + resto + " " + prep3 + " " + carga

k = 60
k1 = 0
for i in range(0, len(texto)):
    if(texto[i] == " "):
        k1 = i

    if(i == k - 1):
        break

texto1 = texto[0:k1+1]
texto2 = texto[k1::]

pos_x1 = 420 - 6.2*len(texto1)
pos_x2 = 420 - 6.2*len(texto2)

pos_y1 = 220
pos_y2 = pos_y1 - 30

cnv.drawString(pos_x1, pos_y1, texto1)
cnv.drawString(pos_x2, pos_y2, texto2)
cnv.save()