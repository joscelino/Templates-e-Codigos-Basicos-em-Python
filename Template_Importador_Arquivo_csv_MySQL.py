# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Template de importacao de dados do MySql
"""
# Importacao das bibliotecas
import pymysql

# Parametros de conexao no MySql
host = ''
id_user = ''
password = ''
data_base = ''

# Criando variavel para receber importacao
base = ' '

# Criando variavel de conexao
conexao = pymysql.connect(host=host, user=id_user, passwd=password, db=data_base)

# Criando cursores
cursor = conexao.cursor()
cursorVendas = conexao.cursor()
cursorVendasProdutos = conexao.cursor()

# Efetuando comandos no MySql
cursorVendas.execute('select * from ------')
for vendas in cursorVendas:
    print(vendas)
    quantidade = cursorVendasProdutos.execute('-------comando SQL-----------')
    i = 1
    for produtos in cursorVendasProdutos:
        print(produtos)
        
        if (i == quantidade):
            base = base + produtos[0]
        else:
            # Inserindo virgula entre os itens
            base = base + produtos[0] + ','
        i += 1
    base = base + '\n'

# Importando arquivo CSV do MySQL
arquivo = open("nome_arquivo.csv", "w")
arquivo.write(base)
arquivo.close()

# Encerrando conexao
cursor.close()
cursorVendas.close()
cursorVendasProdutos.close()
conexao.close()