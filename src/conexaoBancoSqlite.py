import sqlite3

##Método cria uma nova conexão, caso a tabela de venda não exista, ela é criada.
def conectar():
    conn =sqlite3.connect("Banco.db")
    cursor=conn.execute(''' 
                        create table if not exists relatorio(
                            dataVenda datetime,
                            faturamento real,
                            custo real,
                            lucro real
                        )                       
                        ''')
    return conn
    
    
    
##Método de registro de Relatorio
def registrarRelatorio(faturamento,custo,lucro):
    cursor=conectar()
    cursor.execute(f''' 
                              insert into relatorio (dataVenda,faturamento,custo,lucro) values (datetime('now'),{faturamento},{custo},{lucro})
                              ''')
    cursor.commit()
    cursor.close()
    
    
    
    
    

