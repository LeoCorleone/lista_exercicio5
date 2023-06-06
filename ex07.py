# 7- Tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre qual é o maior valor existente na matriz desconsiderando os elementos da diagonal principal.

import random

coluna = []
for ix in range(10):
    linha = []
    for j in range(10):
        linha.append(random.randint(10, 50))
    coluna.append(linha)


for linha in coluna:
    print(linha)


maior_valor = None
for i in range(len(coluna)):
    for j in range(len(coluna[i])):
        if i != j:
            valor = coluna[i][j]
            if maior_valor is None or valor > maior_valor:
                maior_valor = valor


print("O maior valor da diagonal:", maior_valor)