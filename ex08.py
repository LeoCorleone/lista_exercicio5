# 8- Tendo uma matriz 5×5 preenchida com valores aleatórios entre 0 e 99, mostre qual é o segundo maior valor existente na matriz.

import random

coluna = []
for ix in range(5):
    linha = []
    for j in range(5):
        linha.append(random.randint(0, 99))
    coluna.append(linha)

# Imprimindo a matriz
print("Matriz:")
for linha in coluna:
    print(linha)

# Encontrando o segundo maior valor
maior = float('-inf')
segundo = float('-inf')

for linha in coluna:
    for valor in linha:
        if valor > maior:
            segundo = maior
            maior = valor
        elif valor > segundo and valor < maior:
            segundo = valor

print("Segundo maior valor:", segundo)