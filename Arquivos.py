## Abrindo um arquivo ##

arquivo = open("Ola mundo.txt") # Abrir arquivo

texto_completo = arquivo.read()

print(texto_completo)

## Criando um arquivo e editando ##

w = open("arquvio2.txt", "w") ## Criar arquivo

w.write("Este e o meu arquivo")

w.close() # Fechar aquivo
