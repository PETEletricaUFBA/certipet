class Template:

    def __init__(self, modelo):
        if(modelo == "pet"):
            self.fonte_nomes = "./Template/Fontes/Lucida Bright Regular.ttf"
            self.fonte_texto = "./Template/Fontes/BankGothic Md BT Medium.ttf"
            self.k1 = 7.7
            self.k2 = 6
            self.k3 = 60
            self.k4 = 30
            self.k5 = 0
            self.k6 = 0
            self.texto1 = ["O PET Engenharia Elétrica UFT Declara que"]
            self.tamanho_1 = 20
            self.tamanho_2 = 30
            self.cor1 = (0.3, 0.3, 0.3)
            self.cor2 = (0, 0.8, 0.8)
            self.pos_header = (170, 340)
            self.pos_nome = (420, 280)
            self.pos_bottom = (420, 220)
            self.fundo = "PET.png"

        elif(modelo == "liaam"):
            self.fonte_nomes = "Lucida Bright.ttf"
            self.fonte_texto = "SourceSansPro-Regular.ttf"
            self.k1 = 5.8
            self.k2 = 3.5
            self.k3 = 60
            self.k4 = 20
            self.k5 = 4
            self.k6 = 20
            self.texto1 = ["A Liga Acadêmica de Automação por Microcontroladores", "certifica que o(a) Sr(a)"]
            self.tamanho_1 = 16
            self.tamanho_2 = 22
            self.cor1 = (0.3, 0.3, 0.3)
            self.cor2 = (0.22, 0.25, 0.35)
            self.pos_header = (440, 340)
            self.pos_nome = (425, 240)
            self.pos_bottom = (420, 210)
            self.fundo = "LIAAM.png"

    def retornar_fontes(self):
        return (self.fonte_nomes, self.fonte_texto)

    def retornar_constantes(self):
        return (self.k1, self.k2, self.k3, self.k4, self.k5, self.k6)

    def retornar_texto1(self):
        return self.texto1

    def retornar_fundo(self):
        return self.fundo

    def retornar_tamanho_fontes(self):
        return (self.tamanho_1, self.tamanho_2)

    def retornar_cores(self):
        return (self.cor1, self.cor2)

    def retornar_posicoes(self):
        return (self.pos_header, self.pos_nome, self.pos_bottom)