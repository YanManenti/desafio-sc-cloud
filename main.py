import Fibonacci
import Primo

def readNumberHandling(text, errortext):
    try:
        return int(input(text))
    except ValueError:
        print(errortext)

def handleResults(func, valor):
    try:
        print(func(valor))
    except ValueError as valueErrorTxt:
        print(valueErrorTxt)

escolha = -1
while escolha != 5:
    print(f"Opções:\n"
        f"  1. Fibonacci Linear\n"
        f"  2. Fibonacci Recursivo\n"
        f"  3. Primo Linear\n"
        f"  4. Primo Recursivo\n"
        f"  5. Sair")

    errorText = "Erro ao ler sua opção."
    escolha = readNumberHandling("Escolha uma opção: ",errorText)
    match escolha:
        case 1:
            posicaoFinal = readNumberHandling("Qual a posição escolhida: ",errorText)
            handleResults(Fibonacci.fibonacciLinear,posicaoFinal)
        case 2:
            posicaoFinal = readNumberHandling("Qual a posição escolhida: ",errorText)
            handleResults(Fibonacci.fibonacciRecursiva,posicaoFinal)
        case 3:
            valorFinal = readNumberHandling("Qual o valor final escolhido: ",errorText)
            handleResults(Primo.primoLinear, valorFinal)
        case 4:
            valorFinal = readNumberHandling("Qual o valor final escolhido: ",errorText)
            handleResults(Primo.primoRecursivo,valorFinal)
        case 5:
            exit()
        case _:
            print("Opção inválida. Tente novamente.")
    input("Pressione Enter para continuar...")
    print("-----------------------------------------")
