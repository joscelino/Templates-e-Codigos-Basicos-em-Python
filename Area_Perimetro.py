# -*- coding: utf-8 -*-
"""
Template simples para calculo de area e perimetro do circulo
"""
# Importacao das bibliotecas
import math

# Definicao da classe
class circulo:
    def __init__(self, raio):
        self.raio = raio
    @property
    def area(self):
        a = math.pi * (self.raio )** 2
        return a
    @property
    def perimetro(self):
        p = 2 * math.pi * self.raio
        return p
    
# Testando
c = circulo(4.0)
c.raio
area = c.area
perimetro = c.perimetro
