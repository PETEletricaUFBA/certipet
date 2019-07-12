import certificado as cert
import evento as evento
import os


diretorios = os.listdir("./Listas")
total = len(diretorios)
for i in range(0, total):
    print("Gerando Certificados do Evento %d / %d" %(i + 1, total))
    diretorio = diretorios[i]
    eve = evento.Evento(diretorio)
    eve.criar_diretorio()
    certificado = cert.Certificado(eve)
    certificado.gerar()
    print("Gerado")