# Crie um algoritmo que leia um valor e a partir disso faça: (1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado; (2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; (3) se for os valores 6, 7 e 8, mostre o valor dividido 9.

def muda(num):
    if num <= 3:
        return num**2
    elif num == 4 or num == 9:
        return num**(1/2)
    elif num == 6 or num == 7 or num == 8:
        return num/9
    else:
        return "Você digitou um número errado"

num = int(input("Digite um número qualquer entre 1 e 9: "))
result = muda(num)
print(result)