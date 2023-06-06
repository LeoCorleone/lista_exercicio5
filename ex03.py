# 3- Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20 
# posições. Crie uma função que recebe o vetor preenchido e substitua todas as ocorrências de 
# valores negativos por zero, as ocorrências de valores menores do que 10 por 1 e as demais 
# ocorrências por 2.

lista = []

def substituicao(num:int):
    if num < 0:
        num = 0
        lista.append(num)
    elif num < 10:
        num = 1
        lista.append(num)
    else:
        num = 2
        lista.append(num)

for ix in range(0, 5):
    num = int(input("Digite um número qualquer: "))
    substituicao(num)
print(lista)