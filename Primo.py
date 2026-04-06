
# Essa função é recursiva e uma a função auxiliar "primoCheck", também recursiva, para calcular os primos.
# Difere da função pedida, pois são duas funções, entretanto é mais organizada.
def primoRecursivo(valorFinal, valorAtual=2, resultado=None):
    if resultado is None or resultado == 0:
        resultado = []
    if valorFinal is None:
        raise ValueError("Valor inexistente.")
    if valorFinal < 2:
        print("Valor inválido.")
        return []
    if valorAtual > valorFinal:
        return resultado


    if recursivoPrimoCheck(valorAtual):
        resultado.append(valorAtual)

    return primoRecursivo(valorFinal, valorAtual+1, resultado)

def recursivoPrimoCheck(valor, inicial=2):
    if valor < inicial:
        return False
    if valor == inicial:
        return True
    if valor % inicial == 0:
        return False

    return recursivoPrimoCheck(valor, inicial+1)




def primoLinear(valorFinal):
    if valorFinal is None:
        raise ValueError("Valor inexistente.")
    if valorFinal < 2:
        print("Valor inválido.")
        return []

    resultado = []
    for numero in range(2, valorFinal+1):
        if linearPrimoCheck(numero):
            resultado.append(numero)

    return resultado

def linearPrimoCheck(numero):
    primoFlag = True
    for i in range(2, numero + 1):
        if i == numero:
            continue
        if numero % i == 0:
            primoFlag = False
            break

    return primoFlag