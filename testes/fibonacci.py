max = 5

def fibonacci(maximo):
    num = [0, 1]
    while len(num) < maximo:
        num.append(num[-1] + num[-2])
    return num

print(fibonacci(max))