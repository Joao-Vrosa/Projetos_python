# Desenvolva um algoritmo para ler a temperatura em graus Celsius e apresentá-la 
# convertia em graus Fahrenheit (conforme exemplo abaixo).

# Digite a temperatura em graus Celsius: 32
# Portanto 32º graus Celsius é equivalente a 89.6 Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))

f = (9 * celsius + 160) / 5

print("Portanto", celsius, "º", "graus Celsius é equivalente a", f, "Fahrenheit.")


