import time

# Função Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Função Selection Sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[min_idx] > lista[j]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

# Crie uma variável do tipo lista
palavras = list()

# Com a instrução with, leia o conteúdo do arquivo “texto.txt”, percorrendo linha-a-linha
with open("texto.txt", "r") as arquivo:
    for linha in arquivo:
        # Separe cada linha lida em palavras e atribua à lista
        palavras.extend(linha.split())

# Bubble Sort
bubble_palavras = palavras.copy()
start_time = time.time()
bubble_sort(bubble_palavras)
bubble_time = time.time() - start_time
print("Bubble Sort:", bubble_palavras)
print("Tempo de execução (Bubble Sort):", bubble_time, "segundos")

# Selection Sort
selection_palavras = palavras.copy()
start_time = time.time()
selection_sort(selection_palavras)
selection_time = time.time() - start_time
print("\nSelection Sort:", selection_palavras)
print("Tempo de execução (Selection Sort):", selection_time, "segundos")

# Método nativo sort()
native_palavras = palavras.copy()
start_time = time.time()
native_palavras.sort()
native_time = time.time() - start_time
print("\nMétodo nativo Sort:", native_palavras)
print("Tempo de execução (Método nativo Sort):", native_time, "segundos")

# Escolha o algoritmo mais eficiente e salve as palavras ordenadas em um novo arquivo
with open("palavras_ordenadas.txt", "w") as arquivo_saida:
    for palavra in native_palavras:  # Escolhi o método nativo pela melhor performance
        arquivo_saida.write(palavra + "\n")
