# Problema Extra 8 - Raiz e Quadrado

# Escreva um algoritmo de um programa que o usuário possa inserir 2 números. 
# O sistema deverá calcular o quadrado do menor número e a raiz do maior número. 
# Se os números forem iguais, imprimir “números iguais”

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))


if valor1 < valor2:
    print("O quadrado de", valor1, "e" , valor1 * valor1)
elif valor2 < valor1:
    print("O quadrado de", valor2, "e" , valor2 * valor2)

if valor1 > valor2:
    print("A raiz de", valor1, "e", valor1 ** 0.5)
elif valor2 > valor1:
    print("A raiz de", valor2, "e", valor2 ** 0.5)

if valor1 == valor2:
    print("Numeros iguais")

