# Problema Extra 10 - Lucro do Comerciante

# Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% 
# se o valor da compra for menor que R$20,00; caso contrário, o lucro será de 30%. 
# Escreva um algoritmo e o fluxograma de um programa que o usuário possa inserir o 
# valor do produto e o sistema exiba o valor da venda.

valor_produto = float(input("Insira o valor do seu produto: "))


if valor_produto < 20:
    print(valor_produto + 0.45 ** 100)

else:
    print(valor_produto + 0.30 ** 100)

