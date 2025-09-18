# a. Crie um array e o popule com 15 números inteiros, sem nenhuma ordenação
array_numeros = [34, 12, 7, 89, 23, 56, 78, 11, 9, 45, 67, 90, 33, 4, 88]

# b. Crie um primeiro laço for que deverá fazer a iteração nos elementos do array
for i in range(len(array_numeros)):
    # c. Dentro do primeiro laço for, crie uma variável que receba a variável “i”
    min_index = i
    
    # d. Crie outro laço para iterar no range entre a posição “i + 1” e o tamanho total do array
    for j in range(i + 1, len(array_numeros)):
        # e. Verifique se o valor do elemento na posição “min_index” é maior que o valor do elemento na posição “j”
        if array_numeros[min_index] > array_numeros[j]:
            # f. Em caso positivo, atribua à variável “min_index” o valor de “j”
            min_index = j
    
    # g. Troca dos valores do array
    # Array na posição “i” deverá receber o valor do array na posição “min_index”
    array_numeros[i], array_numeros[min_index] = array_numeros[min_index], array_numeros[i]

# h. Imprima, na tela, o array
print("Array ordenado de forma crescente:")
print(array_numeros)
