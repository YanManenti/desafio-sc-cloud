
# Essa função é recursiva e uma a função auxiliar "primoCheck", também recursiva, para calcular os primos.
# Difere da função pedida, pois são duas funções, entretanto é mais organizada.
def primoRecursivo(valorFinal, valorAtual=2, resultado=None):
    if valorFinal < 2:
        return "Valor inválido"
    if resultado is None:
        resultado = []
    if valorAtual > valorFinal:
        return resultado

    if primoCheck(valorAtual):
        resultado.append(valorAtual)

    return primoRecursivo(valorFinal, valorAtual+1, resultado)

def primoCheck(valor, inicial=2):
    if valor < inicial:
        return False
    if valor == inicial:
        return True
    if valor % inicial == 0:
        return False
    return primoCheck(valor, inicial+1)


def primoLinear(valorFinal):
    if valorFinal < 2:
        return "Valor inválido"
    if valorFinal <= 1:
        return []

    resultado = []
    for numero in range(2, valorFinal+1):
        primoFlag = True
        for i in range(2, numero+1):
            if i == numero:
                continue
            if numero % i == 0:
                primoFlag = False
                break
        if primoFlag:
            resultado.append(numero)

    return resultado