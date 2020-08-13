import pyodbc

def conexionsql_MarketplaceDB_ProjectC(query):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=database.server.develop.agrofy.com;DATABASE=MarketplaceDB.ProjectC;UID=;PWD=')
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute(query)
    for data in cursor:
        print(data)
    return data

def conexionsql_MarketplaceDB_Integration(query):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=database.server.develop.agrofy.com;DATABASE=MarketplaceDB.Integration;UID=;PWD=')
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute(query)
    for data in cursor:
        print(data)
    return data

def conexionsql_AccountsDB_Integration(query):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=database.server.develop.agrofy.com;DATABASE=Agrofy.AccountsDB.Integration;UID=;PWD=')
    cursor = conn.cursor()
    cursor = conn.cursor()
    cursor.execute(query)
    for data in cursor:
        print(data)
    return data


ResultadoConsulta =  conexionsql_AccountsDB_Integration("select top 1 code  from  UserCodes ORDER BY UserId DESC")
print(ResultadoConsulta)
Codigo = ResultadoConsulta[0]
print(Codigo)