import sqlite3
import os
from shutil import copyfile
from pathlib import Path

def openDb(dbPath):
    """
    Open a database connection for downstream use

    Parameters:
        dbPath:
            path to source database that is copied
            for local use

    Returns:
        conn:
            connection to database
    """

    #set path of output folder where copy of original db will go with summary and plot(s)
    path = str(os.getcwd()) + "/output"
    
    if not os.path.exists(path):
        os.mkdir(path)
        
    dbPath_out = path + "/" + Path(dbPath).stem + ".db"

    #create copy in local output folder
    copyfile(dbPath, dbPath_out)
    
    try:
        conn = sqlite3.connect(dbPath_out)    
    except Error as e:
        print(e)

    return conn
