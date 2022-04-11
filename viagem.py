# Problema Extra 5 - Viagem

# Elaborar um algoritmo para efetuar o cálculo da quantidade de litros de gasolina gasta em uma viagem,
# sabendo-se que o carro faz 12 km com um litro.
# Deverão ser fornecidos pelo usuário o tempo gasto na viagem (em horas) e a velocidade média (em km/h).

# Entrada
tempo_viagem = float(input("Quanto tempo foi gasto na viagem(em horas)? "))
velocidade_media = float(input("Qual a velocidade média do carro durante a viagem(em km/h)? "))

# Processamento
distancia = tempo_viagem * velocidade_media # FORMULA -> D = T * V
litros = distancia / 12 # FORMULA -> L = D / 12

# Saida
print("O tempo gasto na viagem foi de", tempo_viagem, "horas.")
print("A velocidade média durante a viagem foi de", velocidade_media, "km/h.")
print("A distancia percorrida na viagem foi de", distancia, "km.")
print("Foi gosto um total de", litros, "litros de gasolina na viagem.")

