# Desenvolva o algoritmo e o fluxograma de um programa que permita que o usuário insira dois valores inteiros.
# O programa então imprime na tela o maior valor dentre os dois valores inseridos. Além disso, deve mostrar se os valores são iguais.

valor1 = float(input("Digiteu um número: "))
valor2 = float(input("Digite mais um número: "))

if valor1 > valor2:
    print("O primeiro valor é maio que o segundo valor")
    
elif valor1 < valor2:
    print("O primeiro valor é menor que o segundo valor")

else:
    print("Os valores são iguais.")