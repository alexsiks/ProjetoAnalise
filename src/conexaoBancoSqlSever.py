import pyodbc

# String de Conexão de dados para Sql.
dados_conexao=(
    '''
    Driver={SQL Server};
    Server=192.168.2.4;
    Database=RELATORIO_VENDA;    
    '''
    )

conexao=pyodbc.connect(dados_conexao)
print("Conexão realizada")
cursor=conexao.cursor()

#Função de Inserção de dados com Sql.
def registrarRelatorio(faturamento,custo,lucro):
    comando = f"insert into RELATORIO(DATA_VENDA,faturamento,custo,lucro) values (GETDATE(),{faturamento},{custo},{lucro})"
    cursor.execute(comando)
    cursor.commit()
    conexao.close()