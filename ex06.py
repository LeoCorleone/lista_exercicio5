# 6-  Tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre a média dos elementos da diagonal secundária.

import random

coluna = []
for ix in range(10):
    linha = []
    for j in range(10):
        numero = random.randint(10, 50)
        linha.append(numero)
    coluna.append(linha)

soma = 0
for ix in range(10):
    soma += coluna[ix][9 - ix]

media = soma / 10

print("Média da diagonal secundária:", media)