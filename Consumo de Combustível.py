# Problema 17 - Consumo de Combustível

# Escreva um algoritmo que leia o percurso em km, o tipo de carro e informe o consumo estimado de combustível (em litros).
# Sabe-se que um carro tipo A faz 12 km com um litro de gasolina, um tipo B faz 9km e o tipo C, 8km por litro.

# Obs.: Aceitar o tipo em letras maiúsculas ou minúsculas (ex.: “C” ou “c”)

percurso = float(input("Digite o percurso percorrido pelo carro(Km): "))

tipoCarro = str(input("Digite o tipo do seu carro: "))

tipoA = round((percurso / 12),2)
tipoB = round((percurso / 9),2)
tipoC = round((percurso / 8),2)


if tipoCarro == "A" or tipoCarro == "a":
    print("Foi gasto", tipoA, "litros de gasolina.")
    
elif tipoCarro == "B" or tipoCarro == "b":
    print("Foi gasto", tipoB, "litros de gasolina.")

elif tipoCarro == "C" or tipoCarro == "c":
    print("Foi gasto", tipoC, "litros de gasolina.")
    
else:
    print("Tipo de carro inexistente.")