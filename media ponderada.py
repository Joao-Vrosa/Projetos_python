# MÉDIA PONDERADA

# Entrada
valor1 = float(input("Digite o primeiro número: "))

valor2 = float(input("Digite o segundo número: "))

valor3 = float(input("Digite o terceiro número: "))

valor4 = float(input("Digite o quarto número: "))

# Variaveis criadas para facilitar, caso precise alterar o valor da mesma.
# Levar em consideracao que, se fosse um codigo maior o Dev teria que ir no meio do programa para
# mudar o valor.

P1 = 1
P2 = 2
P3 = 3
P4 = 4

# Processamento
soma = float(valor1 * P1 + valor2 * P2 + valor3 * P3 + valor4 * P4) /(P1+P2+P3+P4)

# Saida
print("A média ponderada destes valores é: ", soma)