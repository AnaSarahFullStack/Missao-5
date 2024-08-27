# Abra um arquivo de texto, ainda não existente, chamado “texto.txt” e o atribua a uma variável
arquivo = open("texto.txt", "w")

# Crie uma lista usando a sintaxe: texto = list();
texto = list()

# Utilizando o método “append”, atribua algumas frases para a lista
texto.append("Esta é a primeira frase.\n")
texto.append("Aqui está a segunda frase.\n")
texto.append("E finalmente, a terceira frase.\n")

# Escreva, no arquivo aberto, o conteúdo da lista
arquivo.writelines(texto)

# Feche o arquivo após a escrita
arquivo.close()
