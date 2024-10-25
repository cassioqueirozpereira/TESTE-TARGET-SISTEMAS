def primo(num):
    contador = num - 1
    if num < 1:
        return print(f"{num} não é primo")
    while contador > 1:
        primo = num % contador
        if primo == 0:
            return print(f"{num} não é primo")
        contador -= 1
    return print(f"{num} é número primo")

primo(17)