# Desenvolva o algoritmo e o fluxograma de um programa que
# permita que o usuário insira um número. O programa então
# deve informar se o número é positivo, negativo ou nulo.

numero = float(input("Insira um número: "))

if numero == 0:
    print("Seu numero é nulo.")

elif numero > 0:
    print("Seu número é positivo.")

elif numero < 0:
    print("Seu número é negativo")