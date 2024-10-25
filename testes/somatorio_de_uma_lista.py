tamanho_da_lista = int(input("Digite quantos números vai querer por na lista: "))
contador = 0
lista = []
while contador < tamanho_da_lista:
    lista.append(int(input(f"Digite o {contador + 1}º número: ")))
    contador += 1

def soma(num):
    total = 0
    for n in num:
        total += n

    return total

print(f"a soma da lista é: {soma(lista)}")