import os
from cauculo import caucularLucro
import conexaoBancoSqlite
import conexaoBancoSqlSever

os.system('cls')

#Entrada de dados
faturamento=float(input("INFORME O VALOR DO FATURAMENTO: "))
custo=float(input("INFORME O VALOR DE CUSTO: "))
lucroCauculado=caucularLucro(faturamento,custo)


##Conexão Sqlite
conexaoBancoSqlite.registrarRelatorio(faturamento,custo,lucroCauculado)

##Conexão Sql sever
conexaoBancoSqlSever.registrarRelatorio(faturamento,custo,lucroCauculado)

print('''\nLUCRO: ''',lucroCauculado)
