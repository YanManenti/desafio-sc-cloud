import Fibonacci
import Primo

escolha = -1
while escolha != 5:
    print(f"Opções:\n"
        f"  1. Fibonacci Linear\n"
        f"  2. Fibonacci Recursivo\n"
        f"  3. Primo Linear\n"
        f"  4. Primo Recursivo\n"
        f"  5. Sair")

    try:
        escolha = int(input("Escolha uma opção: "))
    except ValueError:
        print("Erro ao ler sua opção, insira um numero inteiro")

    match escolha:
        case 1:
            posicaoFinal = int(input("Qual a posição escolhida: "))
            print(Fibonacci.fibonacciLinear(posicaoFinal))
        case 2:
            posicaoFinal = int(input("Qual a posição escolhida: "))
            print(Fibonacci.fibonacciRecursiva(posicaoFinal))
        case 3:
            valorFinal = int(input("Qual o valor final escolhido: "))
            print(Primo.primoLinear(valorFinal))
        case 4:
            valorFinal = int(input("Qual o valor final escolhido: "))
            print(Primo.primoRecursivo(valorFinal))
        case 5:
            exit()
