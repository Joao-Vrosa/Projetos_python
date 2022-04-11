# Problema Extra 9 - Ordernar Números
# Escreva um algoritmo de um programa que o usuário possa inserir 3 números diferentes. 
# O sistema deverá exibir os números em ordem crescente.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

lista = [valor1, valor2, valor3]

lista.sort() # Ordenou a lista de maneira crescente

print(lista)

