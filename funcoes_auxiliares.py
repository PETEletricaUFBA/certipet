def dividir_linhas(texto, qtd_limite):
    contador = 0
    ultimo_contador = 0
    ultimo_espaco = 0
    retorno = []
    for i in range(0, len(texto)):
        if (texto[i] == " "):
            ultimo_espaco = i

        if (contador == qtd_limite):
            retorno.append(texto[ultimo_contador:ultimo_espaco + 1])
            ultimo_contador = ultimo_espaco
            contador -= ultimo_espaco

        elif (i == len(texto) - 1):
            retorno.append(texto[ultimo_contador::])

        else:
            contador += 1

    return retorno