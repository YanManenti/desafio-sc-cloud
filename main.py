import Fibonacci
import Primo

def readNumberErrHandling(text, errortext):
    try:
        return int(input(text))
    except ValueError:
        print(errortext)

escolha = -1
while escolha != 5:
    print(f"Opções:\n"
        f"  1. Fibonacci Linear\n"
        f"  2. Fibonacci Recursivo\n"
        f"  3. Primo Linear\n"
        f"  4. Primo Recursivo\n"
        f"  5. Sair")

    errorText = "Erro ao ler sua opção, insira apenas um numero inteiro"
    escolha = readNumberErrHandling("Escolha uma opção: ",errorText)
    match escolha:
        case 1:
            posicaoFinal = readNumberErrHandling("Qual a posição escolhida: ",errorText)
            print(Fibonacci.fibonacciLinear(posicaoFinal))
        case 2:
            posicaoFinal = readNumberErrHandling("Qual a posição escolhida: ",errorText)
            print(Fibonacci.fibonacciRecursiva(posicaoFinal))
        case 3:
            valorFinal = readNumberErrHandling("Qual o valor final escolhido: ",errorText)
            print(Primo.primoLinear(valorFinal))
        case 4:
            valorFinal = readNumberErrHandling("Qual o valor final escolhido: ",errorText)
            print(Primo.primoRecursivo(valorFinal))
        case 5:
            exit()

    input("Pressione Enter para continuar...")
