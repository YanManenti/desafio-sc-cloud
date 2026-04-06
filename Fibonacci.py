def fibonacciRecursiva(posicaoFinal):
    if posicaoFinal is None or posicaoFinal < 0:
        return "Posição inválida."

    if posicaoFinal == 0 or posicaoFinal == 1:
        return posicaoFinal

    return fibonacciRecursiva(posicaoFinal-1) + fibonacciRecursiva(posicaoFinal-2)


def fibonacciLinear(posicaoFinal):
    if posicaoFinal is None or posicaoFinal < 0:
        return "Posição inválida."

    resultado = [0, 1]
    for numero in range(1,posicaoFinal):
        resultado.append(resultado[numero] + resultado[numero-1])

    return resultado[posicaoFinal]