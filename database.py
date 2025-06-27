import pyodbc

def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=your-server-name.database.windows.net;'
        'DATABASE=your-db-name;'
        'UID=your-username;'
        'PWD=your-password'
    )
