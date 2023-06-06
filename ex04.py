# 4- crie um algoritmo que solicite 3 valores que representarão os lados de um triângulo. Considere que não importa a ordem que serão fornecidos os valores, podendo ser fornecido primeiro a hipotenusa e depois os catetos, ou primeiro os catetos e depois a hipotenusa, etc. Crie também uma função que recebe o vetor e retorna se os lados informados formam um triângulo retângulo. Você pode utilizar o teorema de Pitágoras para auxiliar na resolução: hiponusa2 = cateto12 + cateto22.

def trianguloRetangulo(lad1,lad2,lad3):
    if ((lad1**2) == ((lad2**2) + (lad3**2))) or ((lad2**2) == ((lad1**2) + (lad3**2))) or ((lad3**2) == ((lad1**2) + (lad2**2))):
        return "É um triangulo retângulo!"
    else:
        return "Não é um triangulo retângulo!"

lad1 = int(input("Insira o primeiro lado: "))
lad2 = int(input("Insira o segundo lado: "))
lad3 = int(input("Insira o terceiro lado: "))
result = trianguloRetangulo(lad1,lad2,lad3)
print(result)