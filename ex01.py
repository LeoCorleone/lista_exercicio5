# 1-  Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 30 
# posições. Crie uma função que recebe o vetor preenchido e substitua todas as ocorrência de 
# valores positivos por 1 e todos os valores negativos por 0.

lista = []
def substituicao(num: int):
    if num < 0:
        num = 0
        lista.append(num)
    else:
        num = 1
        lista.append(num)
    
for ix in range (0, 5):
    num = int(input("Digite um número inteiro qualquer: "))
    substituicao(num)
print(lista)