# -*- coding: utf-8 -*-
'''
Codigo para renover itens duplicados em uma sequencia, preservando a ordem.
* Itens passiveis de hash.'''

# Criando a funcao
def dedupe(itens):
    seen = set()
    for item in itens:
        if item not in seen:
            yield item
            seen.add(item)

# Exemplo de aplicacao
# Sequencia
a = [1, 5, 2, 1, 9, 1, 5, 2, 10]

# Executando a funcao
b = list(dedupe(a))

'''
Codigo para renover itens duplicados em uma sequencia, preservando a ordem.
* Itens NAO passiveis de hash.'''

# Criando a funcao
def dedic(itens, key=None):
    seen = set()
    for item in itens:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
# Exemplo de aplicacao
# Dicionario
ab = [{'x':1, 'y': 2}, {'x':1, 'y': 3},  {'x':1, 'y': 2}, {'x':2, 'y': 4}]

# Exemplos
bb = list(dedic(ab, key=lambda d: (d['x'], d['y'])))
bc = list(dedic(ab, key=lambda d: d['x']))


