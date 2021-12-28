import os
from control import cauculo
import model.conexaoBancoSqlite
import model.conexaoBancoSqlSever
os.system('cls')

#Atribuição a Objetos de conexão ao banco de dados-----------------------
conexaoSqlite = model.conexaoBancoSqlite
conexaoSqlServer = model.conexaoBancoSqlSever


#Entrada de dados--------------------------------------------------------
faturamento=float(input("INFORME O VALOR DO FATURAMENTO: "))
custo=float(input("INFORME O VALOR DE CUSTO: "))
lucroCauculado=cauculo.caucularLucro(faturamento,custo)


##Conexão Sqlite
conexaoSqlite.registrarRelatorio(faturamento,custo,lucroCauculado)
##Conexão Sql sever
conexaoSqlServer.registrarRelatorio(faturamento,custo,lucroCauculado)


#Saída de Dados------------------------------------------------------------
print('''\nLUCRO: ''',lucroCauculado)
