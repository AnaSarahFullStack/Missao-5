def bubbleSort(array):
    # Laço for para iterar nos elementos do array
    for i in range(len(array)):
        # Laço for para iterar de dois a dois os elementos do array
        for j in range(0, len(array) - i - 1):
            # Condição para comparar e trocar os elementos adjacentes
            if array[j] > array[j + 1]:
                # Troca os valores dos elementos
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Declarando um array de números com 15 posições
array_numeros = [13, 89, 41, 60, 63, 74, 97, 58, 100, 99, 48, 92, 97, 71, 78]

# Aplicando o método bubbleSort no array
bubbleSort(array_numeros)

# Imprimindo o array ordenado de forma crescente
print("Array ordenado de forma crescente:")
print(array_numeros)
