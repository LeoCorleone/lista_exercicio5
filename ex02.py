# 2- Crie uma função que retorne o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 + … + n/m, para um valor de n definido pelo usuário. Verifique se o valor de n definido pelo usuário é positivo e, caso não seja, solicite outro valor até ser fornecido um valor positivo.

def conta():
    num = int(input("Digite um valor positivo inteiro qualquer: "))
    while num <= 0:
        print("O valor de n deve ser positivo. Tente novamente.")
        num = int(input("Digite um valor positivo inteiro qualquer: "))

    soma = 0
    deno = 3 
    for i in range(2, num + 2):
        soma += i / deno
        deno += 2

    return soma

resultado = conta()
print("O resultado da expressão é: ", resultado)