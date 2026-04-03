def primoRecursivo(valorFinal, valorAtual=2, resultado=None):
    if resultado is None:
        resultado = []
    if valorAtual > valorFinal:
        return resultado

    primoFlag = True
    for primo in resultado:
        if valorAtual % primo == 0:
            primoFlag = False
            break

    if primoFlag:
        resultado.append(valorAtual)

    return primoRecursivo(valorFinal, valorAtual+1, resultado)

def primoLinear(valor):
    if valor < 1:
        return []

    resultado = []
    for numero in range(2, valor):
        primoFlag = True
        for i in range(2, numero-1):
            if numero % i == 0:
                primoFlag = False
        if primoFlag is True:
            resultado.append(numero)

    return resultado