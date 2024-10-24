def fibonacci(n):
    # gera a sequência de Fibonacci até o valor escolhido pelo usuário.
    num = [0, 1]
    while len(num) < n:
        num2 = num[-1] + num[-2]
        num.append(num2)
    return num
posicao_maxima = int(input("\nDigite até que posição do número de fibonacci deseja verificar: "))
def pertence_fibonacci(num3):
    # Verifica se um número pertence à sequência de Fibonacci
    num = fibonacci(posicao_maxima)  # Você pode aumentar esse valor para mais termos
    print(num)
    return num3 in num
# adicionei o método do_while ao programa para o usuário poder testar o
sim = 1

while sim == 1:
    # Solicita um número ao usuário
    numero = int(input("\nDigite o número que deseja verificar: "))

    # Verifica se o número pertence à sequência de Fibonacci
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
    sim = int(input("\nSe quiser continuar a testar outros números digite 1, se não digite 0: "))