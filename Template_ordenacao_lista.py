# -*- coding: utf-8 -*-
# Template para encontrar os N maiores e menores de uma lista
# Importacao da biblioteca
import heapq

# Exemplo 1
# Lista
lista = [1, 8, 2, 23, -4, 87, 23, 18, 23, 0.5, 2, 43, 11, 111, 11, 0.07]

# Imprimindo os n maiores forma 1
print(heapq.nlargest(3, lista))
# Imprimindo os n menores forma 1
print(heapq.nsmallest(3, lista))

# Imprimindo o menor 
print(min(lista))
# Imprimindo o maior 
print(max(lista))

# Ordenando a lista inteira
lista_ordenada = sorted(lista)

# Exemplo 2
# Lista 2
portfolio = [
    {'ativo': 'IBM', 'lucro': 100, 'preco': 17.5},
    {'ativo': 'MST', 'lucro': 90, 'preco': 52.5},
    {'ativo': 'AAPL', 'lucro': 75.5, 'preco': 45.3},
    {'ativo': 'VALE', 'lucro': 17.02, 'preco': 102.5},
    {'ativo': 'AMZN', 'lucro': 87.5, 'preco': 75.02},
    {'ativo': 'CNN', 'lucro': 31.1, 'preco': 69.73},
    {'ativo': 'SAP', 'lucro': 77.77, 'preco': 60.52}]

# Ordenacao
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['preco'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['preco'])

