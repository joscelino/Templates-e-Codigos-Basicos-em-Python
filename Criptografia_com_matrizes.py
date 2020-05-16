# -*- coding: utf-8 -*-
"""
Criptografia com a utilizacao de matrizes 
"""
# importar bibliotecas:
import numpy as np
from numpy.linalg import inv

# Definir matriz de codificação
C = np.array(([1,2],[3,4]))

# Matriz para decodificação -> inversa de C
D = inv(C)

# dicionário para a referênciação dos números com letras
cod = {1:'A', 2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',
          12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',
          23:'W',24:'X',25:'Y',26:'Z',27:'.',28:',',29:'_'}

cod

def texto2numeros(texto):
    nu = []
    # para deixar a matriz com duas linhas completa:
    if(len(texto)%2 != 0):
        texto = texto+'_' # Precisamos add _ para completar matriz!
    # transformar letras em números no dicionário
    for ii in texto:
        for j in cod:
            if(cod[j]==ii):
                nu.append(j)
    return nu

def numeros2texto(num):
    Tex = ''
    for i in num:
        Tex = Tex+str(cod[round(i)])
    return Tex

texto = 'JOSCELINO_CELSO_DE_OLIVEIRA'

len(texto)

VT = texto2numeros(texto)

MT = np.array(VT)                  # transformar em array

MSG = MT.reshape(2,int(MT.size/2)) # mensagem em matriz

MC = C.dot(MSG)                    # mensagem codificada

MD = D.dot(MC)                     # mensagem decodificada

msg_d = MD.reshape(1,MD.size)      # matriz da msg transformada em vetor

MSG.shape

print('==MENSAGEM EM MATRIZ=====')
print(MSG)
print('===MENSAGEM CODIFICADA===')
print(MC)
print('==MENSAGEM DECODIFICADA==')
print(MD)
print('=MSG DECODIFICA EM VETOR=')
print(msg_d)
print('====MSG TRANSFORMADA=====')
print(numeros2texto(msg_d[0,:]))

