import os
from cauculo import caucularLucro
import conexaoBanco
import conexaoBancoSqlSever
from datetime import date

os.system('cls')

#Entrada de dados
faturamento=float(input("INFORME O VALOR DO FATURAMENTO: "))
custo=float(input("INFORME O VALOR DE CUSTO: "))
lucroCauculado=caucularLucro(faturamento,custo)
dataVenda=date.today()


##Imprimir dados
conexaoBanco.registrarRelatorio(faturamento,custo,lucroCauculado)
conexaoBancoSqlSever.registrarRelatorio(faturamento,custo,lucroCauculado)

print('''\nLUCRO: ''',lucroCauculado)
