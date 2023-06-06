def contas(num):
    if num == 1 or num == 2:
        resultado = num ** 3
        print("O valor elevado ao cubo é:", resultado)
    elif num % 3 == 0:
        resultado = fatorial(num)
        print("O fatorial de", num, "é:", resultado)
    elif num == 4 or num == 5 or num == 7 or num == 8:
        resultado = num / 9
        print("O valor dividido por 9 é:", resultado)
    else:
        print("Valor inválido")

def fatorial(fat):
    fat = 1
    for i in range(1, fat + 1):
        fat *= i
    return fat

num = int(input("Digite um valor: "))
contas(num)