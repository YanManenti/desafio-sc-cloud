def primeCheck(valor, inicial=2):
    if valor == inicial:
        return True
    if valor % inicial == 0:
        return False
    return primeCheck(valor, inicial+1)

def primoRecursivo(valor):
    resultado = []
    if valor < 2:
        return resultado

    resultado = primoRecursivo(valor-1)

    if primeCheck(valor):
        resultado.append(valor)

    return resultado


def primoLinear(valor):
    if valor < 1:
        return "Número menor ou igual a 1"

    resultado = []
    for numero in range(2, valor):
        primoFlag = True
        for i in range(2, numero-1):
            if numero % i == 0:
                primoFlag = False
        if primoFlag is True:
            resultado.append(numero)

    return resultado