import random

# Passo 1: Criar um array de 15 posições com números inteiros e valores aleatórios, não ordenados
array_inteiros = [random.randint(1, 100) for _ in range(15)]

# Passo 2: Ordenar o array de forma crescente utilizando o método sort
array_inteiros.sort()

# Passo 3: Imprimir o array ordenado de forma crescente
print("Array de números inteiros ordenado de forma crescente:")
print(array_inteiros)

# Passo 4: Ordenar o array de forma decrescente utilizando o método sort com reverse=True
array_inteiros.sort(reverse=True)

# Passo 5: Imprimir o array ordenado de forma decrescente
print("Array de números inteiros ordenado de forma decrescente:")
print(array_inteiros)

# Passo 6: Criar um array de strings com nome, dataNascimento, cpf, rg
array_strings = ["Ana Sara", "15/03/2003", "123.456.789-00", "1234567"]

# Passo 7: Ordenar o array de strings de forma crescente
array_strings.sort()

# Passo 8: Imprimir o array de strings ordenado de forma crescente
print("Array de strings ordenado de forma crescente:")
print(array_strings)

# Passo 9: Ordenar o array de strings de forma decrescente
array_strings.sort(reverse=True)

# Passo 10: Imprimir o array de strings ordenado de forma decrescente
print("Array de strings ordenado de forma decrescente:")
print(array_strings)
