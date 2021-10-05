import pandas as pd
import sqlite3
import os
from shutil import copyfile
from pathlib import Path

def dbRead(dbConn, dbTable):
    '''
    Reads in SQLite database and converts table 
    to pandas dataframe for downstream analysis

    Parameters:
        dbConn:
            connection to database to be used for comparison table

        dbTable:
            Name of table to convert to dataframe

    Returns:
        df:
            Dataframe representing selected table

    Future versions of this will be used in class to 
    read mutliple file types

    '''
        
    df = pd.read_sql_query('SELECT * FROM ' + dbTable, dbConn)
    
    return df


