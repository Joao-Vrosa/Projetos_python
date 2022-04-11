## Calcula Peso ##

# Desenvolva um algoritmo que leia o peso de uma pessoa (em kg), calcule e imprima:

# O peso da pessoa em gramas
# novo peso, em gramas, se a pessoa engordar 12%

# Entrada
peso = float(input("Qual o seu peso: "))

# Processamento
calculo = (peso * 1000) * 12/100

# Saida
print("O seu novo peso em gramas mais 12% e de: ", calculo)