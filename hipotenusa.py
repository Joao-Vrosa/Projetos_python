## Cálculo de hipotenusa ##

# Desenvolva um programa que pergunte o valor dos catetos de um triângulo retângulo e
# imprima o valor da hipotenusa (conforme exemplo abaixo).

# Digite o valor do cateto 1: 3
# Digite o valor do cateto 2: 4

# Portanto, o valor da hipotenusa é: 5


# Entrada
cateto1 = float(input("Digite o valor do cateto 1: "))
cateto2 = float(input("Digite o valor do cateto 2: "))

# Processamento
calculo = (cateto1 ** 2) + (cateto2 ** 2)
hipotenusa = calculo ** 0.5

# Saida
print("Portanto, o valor da hipotenusa é:", hipotenusa)