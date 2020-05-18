# -*- coding: utf-8 -*-
"""
Validacao de IPs utilizando expressoes regulares
"""
# Importacao das bibliotecas
import re

# Criando expressao regular pra 
ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
             25[0-5]        |      # Ranges 250-255
             2[0-4][0-9]    |      # Ranges de 240-249
             1[0-9]{2}      |      # Ranges de 100 - 199
             [1-9][0-9]     |      # Range de 10 - 99
             [0-9]                 # Range de 0-9
        
        )\.
     
    ){3}
        
        (?:
             25[0-5]        |      # Ranges 250-255
             2[0-4][0-9]    |      # Ranges de 240-249
             1[0-9]{2}      |      # Ranges de 100 - 199
             [1-9][0-9]     |      # Range de 10 - 99
             [0-9]                 # Range de 0-9
        
        )$
''', flags=re.VERBOSE)

# Chacagem da validacao de IPs
for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))