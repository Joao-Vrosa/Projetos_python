# Meu primerio código em Python #

print("Olá usuario!")
NomeUser = input("Qual o seu primeiro nome? ")
SobreNome = input("Qual o seu sobrenome? ")
print("Seja bem-vindo(a)", NomeUser,SobreNome + "!")

print("==========")

numero = input("Digite um número: ")
numero = int(numero) # Usar int para numeros inteiros.
numero = numero *2
print("O dobro do número é:", numero)

numero = numero /2
numero = int(numero)
if(numero >= 100): # Se for maior ou igual a 100 ira executar está fução.

 print("O numero", numero, "dividido por 2 é: ", numero /2)

if(numero < 100): # Se for menor que 100 não ira acontecer nada.
  pass # Pass = Vazio/Passar.

print("==========")
print("Obrigado por participar do meu primerio código,",NomeUser + "!")
