# Crie um algoritmo que leia um valor e a partir disso faça: (1) se for um valor negativo, mostre o módulo (valor sem sinal) do valor; (2) se for um valor maior do que 10, solicite outro valor e mostre a diferença entre eles; (3) Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5.

num = float(input("Digite um número qualquer: "))

if num < 0:
    numSemSinal = abs(num)
    print("O número sem sinal é:", numSemSinal)
elif num > 10:
    numRepete = float(input("Digite outro valor: "))
    diferenca = num - numRepete
    print("A diferença entre os valores é:", diferenca)
else:
    resultado = num / 5
    print("O resultado da divisão por 5 é:", resultado)