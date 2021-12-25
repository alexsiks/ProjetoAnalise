import pyodbc


def conectar():
    conn = pyodbc.connect(
        "DRIVER={SQL SERVER};SERVER=192.168.2.4;PORT=3306;DATABASE=PESQUISA;UID=USER;PWD=123;")
    cursor = conn.cursor()
    cursor.execute('''
                create table if not exists RELATORIO(
                    dataVenda datetime,
                    Faturamento money,
                    Custo money,
                    Lucro money
        )''')
    return conn


def registrarRelatorio(faturamento, custo, lucro):
    cursor = conectar()
    cursor.execute(f''' 
                   insert into relatorio(dataVenda,Faturamento,Custo,Lucro) values (getdate(),{faturamento},{custo},{lucro})
                   
                   ''')
    cursor.commit()
    cursor.close()
