# No script “ler.txt.py”:

# a. Crie uma variável e atribua a ela, com o método “open”, o conteúdo do arquivo txt criado acima
arquivo = open("loremipsum.txt", "r")

# b. Imprima, na tela, todo o conteúdo da variável (e, consequentemente, do arquivo txt lido)
conteudo_completo = arquivo.read()
print("Conteúdo completo do arquivo:")
print(conteudo_completo)

# Feche o arquivo após a leitura
arquivo.close()

# c. Reabra o arquivo e imprima a primeira linha do arquivo txt
arquivo = open("loremipsum.txt", "r")
primeira_linha = arquivo.readline()
print("Primeira linha do arquivo:/n")
print(primeira_linha)

# Feche o arquivo após a leitura
arquivo.close()

# d. Reabra o arquivo e imprima os 3 primeiros caracteres do arquivo txt
arquivo = open("loremipsum.txt", "r")
tres_primeiros_caracteres = arquivo.read(3)
print("\nOs 3 primeiros caracteres do arquivo:")
print(tres_primeiros_caracteres)

# Feche o arquivo após a leitura
arquivo.close()

# e. Utilize a instrução “with” para abrir o arquivo, armazenar seu conteúdo numa variável e o imprimir
print("\nConteúdo do arquivo usando 'with':")
with open("loremipsum.txt", "r") as arquivo:
    conteudo_with = arquivo.read()
    print(conteudo_with)