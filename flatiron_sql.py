import sqlite3
import pandas as pd

#function to view the contents of a table
def view_table(tablename, conn):
    """Displays the specified table from the database connection.
    """
    query = f"SELECT * FROM {tablename}"
    df = pd.read_sql(query,conn)
    display(df) 
    
#function to get the contents of a table
def get_table(tablename, conn):
    """Returns the specified table from the database connection.
    """
    query = f"SELECT * FROM {tablename}"
    df = pd.read_sql(query,conn)
    return df

#function to get a list of the table names
def get_table_names(conn):
    """Returns the table names for a given database connection.
    """
    cur = conn.cursor()
    table_names = [res[0] for res in cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""").fetchall()]
    return table_names