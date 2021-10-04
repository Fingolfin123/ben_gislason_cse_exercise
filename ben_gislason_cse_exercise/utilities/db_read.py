import pandas as pd
import sqlite3
import os
from shutil import copyfile
from pathlib import Path

def dbRead(dbPath, dbTable):
    '''
    Reads in SQLite database and converts table 
    to pandas dataframe for downstream analysis

    Parameters:
        dbPath:
            Path of database to be used for comparison table
            this database if first copied to local test directory

        dbTable:
            Name of table to convert to dataframe

    Returns:
        df:
            Dataframe representing selected table

    Future versions of this will be used in class to 
    read mutliple file types

    '''

    dbPath_out = os.path.abspath(os.curdir)+"\\ben_gislason_cse_exercise\\tests\\" + Path(dbPath).stem + ".db"
    copyfile(dbPath, dbPath_out)
    
    try:
        conn = sqlite3.connect(dbPath_out)    
    except Error as e:
        print(e)
        
    df = pd.read_sql_query('SELECT * FROM ' + dbTable, conn)
    
    return df

    conn.close()


