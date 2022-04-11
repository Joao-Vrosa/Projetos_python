# Problema Extra 7 - Verifica Estado

# Escreva um algoritmo de um programa que o usuário possa entrar com a sigla de um estado.
# Caso a sigla seja RJ, imprimir “carioca”, caso SP, imprimir “paulista”, caso MG, imprimir “mineiro” e caso qualquer outra entrada, imprimir “outros estados”

# Obs.: Considerar siglas maiúsculas e minúsculas

sigla = input("Digite a sigla do seu estado: ")


if sigla == "rj":
    print("Carioca")
elif sigla == "RJ":
    print("Carioca")
       
elif sigla == "sp":
    print("Paulista")
if sigla == "SP":
    print("Paulista")
   
elif sigla == "mg":
    print("Mineiro")
if sigla == "MG":
    print("Mineiro")

else:
    print("Outros estados")