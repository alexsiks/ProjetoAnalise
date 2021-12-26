# ProjetoAnalise

1- Projeto de análise de Faturamento, Custo e de Lucro.





def registrarRelatorio(faturamento, custo, lucro):
    cursor = conectar()
    cursor.execute(f''' 
                   insert into relatorio(dataVenda,Faturamento,Custo,Lucro) values (getdate(),{faturamento},{custo},{lucro})
                   
                   ''')
    cursor.commit()
    cursor.close()
