# 5- Faça um algoritmo que solicite ao usuário números e os armazene em uma matriz 6×6. Em seguida, crie um vetor que armazene os elementos da diagonal principal da matriz.

coluna = []
for ix in range(6):
    linha = []
    for j in range(6):
        numero = int(input("Digite um número para a posição {}, {}: ".format(ix, j)))
        linha.append(numero)
    coluna.append(linha)

diagonal = []
for ix in range(6):
    diagonal.append(coluna[ix][ix])

print(diagonal)
