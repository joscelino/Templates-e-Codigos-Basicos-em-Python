# -*- coding: utf-8 -*-
"""
Validador de Senhas usando Regex
"""
# Importacao das bibliotecas
import re

# Expressao regular
senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

# Variavel senha
string = '''
VÁLIDAS
v2Ts7<o9T~}Y
j25TTbjJ:6{<
s`Mu6T;4M1!y
Li`hk6:3WX>3
d.D09}^dI2Vn
SEM MINÚSCULAS
I7^Y3RS^ 9]7
[P6W"83L5V{[
B7=;K8D6_}W5
1B_RT`93R%>1
EZU{7;2&D:64
SEM MINÚSCULAS E NÚMEROS
E}LV`C?X_G:{
AJH[@HD*V~=<
\A~AC{_V~MG 
W<-T}W:QAF'{
~YJ}|FILN>~)
SEM NÚMEROS CARACTERES E MINÚSCULAS
PBDZDPECUDNN
EJQWFWFFDEHY
XRCNLNRHYOZJ
TWIYPLWUDMNN
JMDTJSEPKVON
QUANTIDADE INVÁLIDA (6)
Iu4<1j
1x`P6g
@9t3Ry
qf9_6H
0o`9fO
'''
# Validacao
print(senha_forte_regexp.findall(string))