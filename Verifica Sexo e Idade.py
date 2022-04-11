# Problema Extra 6 - Verifica Sexo e Idade

# Escreva um algoritmo de um programa que o usuário possa entrar com seu nome, sexo e idade.
# Se a pessoa for do sexo feminino e tiver menos que 25 anos, exibir o nome e a mensagem “Aceita”, 
# caso contrário, exibir o nome e a mensagem “Não aceita”.

# Exemplo de saída: Maria aceita; José não aceito.
# Obs.: Aceitar f, F, m e M para sexo.

nome = input("Digite o seu nome: ")
sexo = input("Qual o seu sexo(F/M)? ")
idade = int(input("Digite a sua idade: "))

if sexo == "M" or "m":
    print(nome, "Aceita")

else:
    if sexo == "F" or "f":
        if idade < 25:
            print(nome, "Aceita")
        else:
            print(nome, "Nao aceita")

