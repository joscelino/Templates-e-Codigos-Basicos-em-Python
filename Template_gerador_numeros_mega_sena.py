# -*- coding: utf-8 -*-
"""
Gerador de numeros para mega-sena
"""
import random 


def megasena():
    jogo = []
    while len(jogo) < 6:
        num = random.randint(1, 60)
        if num in jogo:
            continue
        else:
            jogo.append(num)
    return sorted(jogo)
    print(jogo)


lista = megasena()
