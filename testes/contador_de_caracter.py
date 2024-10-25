frase = input("Digite a frase que quiser: ")

objetivo = input("Digite o caracter que deseja saber quantas vezes aparece na frase: ").upper()

contador = frase.upper().count(objetivo)

print(f"\nA frase que tu digitou foi: {frase}\nO caracter a ser contado é: {objetivo}\nEle aparece {contador} vez(es)")