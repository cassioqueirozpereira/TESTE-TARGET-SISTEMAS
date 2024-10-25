x = int(input("digite o número: "))

def impar_par(num):
    num %= 2
    
    if num == 0:
        return print("número é par")
    else:
        return print("número é impar")
    
impar_par(x)