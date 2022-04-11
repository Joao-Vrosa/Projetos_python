## Problema Extra 1 - Área do triângulo ##

# Desenvolva um algoritmo que calcule e imprima a área de um triângulo (conforme exemplo abaixo).
# Digite o valor da base do triângulo (em metros): 10
# Digite o valor da altura do triângulo (em metros):  5
# Obrigado! Portanto para um triângulo de base 10 (m) e altura de 5(m) a área do triângulo 
# é de 25 m².


# Entrada
base = float(input("Digite o valor da base do triângulo (em metros): "))
altura = float(input("Digite o valor da altura do triângulo (em metros): "))

# Processamento
area = (base * altura) / 2

# Saida
print("Obrigado! Portanto para um triângulo de base", base, "(m) e altura de", altura, "(m) a área do triângulo é de", area, "m².")
