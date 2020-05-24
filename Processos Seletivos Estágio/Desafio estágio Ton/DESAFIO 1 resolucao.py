

#importando as bibliotecas necessárias
import pyodbc as pc
import pandas as pd

print (">>Bibliotecas importadas com sucesso :)")



#comando base para nos conectarmos a base de dados SQL localmente no computador do usuário. Alguns cuidados:
#1-o "server" e a "database" dependem da nomenclatura utilizada pelo usuário em seu documento de SQL. No meu caso usei as informações do meu SQL pessoal
#2-o "pc" é uma abreviação da biblioteca pyodbc importando no passo anterior

server = input("Coloque o nome do seu servidor SQL:")
database = input("Coloque o nome da ")

def retornar_conexao_sql():
    server = "DESKTOP-EJF16R5\MSSQL"
    database = "teste"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pc.connect(string_conexao)
    return conexao

conn = retornar_conexao_sql()

print (">>a conexao com o banco de dados foi realizada com sucesso :)")



#função para consultarmos dados do banco (GET)
#para usar esta função, os dados devem ser inseridos como string

def get_dados(coluna, tabela, condicao1, condicao2):
    sql = 'SELECT'+coluna+'FROM'+tabela+'WHERE'+condicao1+'='+condicao2
    dados = pd.read_sql(sql, conn)
    return dados
    print (">>Ta ai sua base de dados, oh :)")


#função para inserirmos dados no banco (PUT)
#para usar esta função, os dados devem ser inseridos como string
#a tabela que deseja ser inputado os valores deve ter, no máximo, 5 colunas

def put_dados(tabela, coluna1, coluna2=None, coluna3=None, coluna4=None, coluna5=None, valores1, valores2=None, valores3=None, valores4=None, valores5=None):
    if coluna2 ==None:    
        sql = 'INSERT INTO'+tabela+'('+coluna1+')'+'VALUES ('+valores1+')'
        dados = pd.read_sql(sql, conn)
        return dados
    
    elif coluna3 ==None:
        sql = 'INSERT INTO'+tabela+'('+coluna1+','+coluna2+')'+'VALUES ('+valores1+','+valores2+')'
        dados = pd.read_sql(sql, conn)
        return dados
    
    elif coluna4 ==None:
        sql = 'INSERT INTO'+tabela+'('+coluna1+','+coluna2+','+coluna3+')'+'VALUES ('+valores1+','+valores2+','+valores3+')'
        dados = pd.read_sql(sql, conn)
        return dados
    
    elif coluna5 ==None:
        sql = 'INSERT INTO'+tabela+'('+coluna1+','+coluna2+','+coluna3+','+coluna4+')'+'VALUES ('+valores1+','+valores2+','+valores3+','valores4+')'
        dados = pd.read_sql(sql, conn)
        return dados
    
    else:
        sql = 'INSERT INTO'+tabela+'('+coluna1+','+coluna2+','+coluna3+','+coluna4+','+coluna5+')'+'VALUES ('+valores1+','+valores2+','+valores3+','valores4+','+valores5+')'
        dados = pd.read_sql(sql, conn)
        return dados
    
    print (">>Você conseguiu colocar seus dados na base de dados :)")
        

#função para excluirmos dados do banco (DELETE)
#para usar esta função, os dados devem ser inseridos como string

def get_dados(coluna, tabela, condicao1, condicao2):
    sql = 'SELECT'+coluna+'FROM'+tabela+'WHERE'+condicao1+'='+condicao2
    dados = pd.read_sql(sql, conn)
    return dados
    print (">>Ta ai sua base de dados, oh :)")


def retornar_conexao_sql():
    server = "DESKTOP-EJF16R5\MSSQL"
    database = "teste"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pc.connect(string_conexao)
    return conexao


dados = pd.read_sql(sql, conn)



