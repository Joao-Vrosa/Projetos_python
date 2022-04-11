## Quanto cobrar por um site? ##

# Valor por hora de trabalho
# Impostos
# Lucro

tempo = float(input("Quanto tempo para o site ficar pronto (em dias)? "))

lucro = 0.15

imposto = 0.19

total = tempo / (1 - imposto - lucro)

print("O valor cobrado por hora e: ",total )

cobrar = total * 30

print(cobrar)