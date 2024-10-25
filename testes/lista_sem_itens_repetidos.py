lista = [1, 5, 3, 2, 7, 8, 1, 4, 6, 10]

def sem_valor_repetido(lista):
    for item in lista:
        contador = lista.index(item)
        while len(lista) > contador + 1:
            if item == lista[contador + 1]:
                lista.pop(contador + 1)
                contador -= 1
            contador += 1
    return print(lista)

print("lista normal")
print(lista)
print("lista depois de tirado os números repetidos")
sem_valor_repetido(lista)