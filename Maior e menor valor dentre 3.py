# Problema 14 - Maior e menor valor dentre 3

# Escreva um algoritmo de um programa que permita que o usuário insira três valores inteiros.
# O programa então imprime na tela o maior e o menor valor dentre os três valores inseridos.
# Além disso, o programa deve mostrar se os valores são iguais.

# Obs.: NÃO é permitido utilizar os operadores lógicos or ou and.

valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))
valor3 = int(input("Digite o valor 3: "))

if valor1 == valor2 == valor3:
    print("Os valores são iguais")
    exit() # Se for verdadeiro finaliza o programa
    
if valor1 >= valor2: # LOGICA -> Verificar qual o maior valor
    if valor1 >= valor3:
        print("Maior valor: ", valor1)
    else:
        print("Maior valor: ", valor3)
else:
    if valor2 >= valor3:
        print("Maior valor: ", valor2)
    else:
        print("Maior valor: ", valor3)
        
if valor1 <= valor2: # LOGICA -> Verificar qual o menor valor
    if valor1 <= valor3:
        print("Menor valor: ", valor1)
    else:
        print("Menor valor: ", valor3)
else:
    if valor2 <= valor3:
        print("Menor valor: ", valor2)
    else:
        print("Menor valor: ", valor3)

