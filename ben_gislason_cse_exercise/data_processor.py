#import modules 
from ben_gislason_cse_exercise.utilities.db_read import dbRead
from ben_gislason_cse_exercise.utilities.calc_tb_stats import calcTBStats
from ben_gislason_cse_exercise.utilities.db_write import dbWrite
from ben_gislason_cse_exercise.utilities.build_plots import plotTables

def DataProcessor(dbPath):
    '''
    DataProcessor reads in SQLite db containing two 
    tables of load data for statistical summary.

    Parameters:
        dbPath: str
            Path to SQLite database file

        tableNames: tuple(str)
            Names of load data tables to be compared. 
            
    Future version may include this as a user 
    input or read from db directly

    '''
    #read data tables from SQLLite and convert to data frames for analysis
    tableNames = ['smaller_bin_consumption_data','larger_bin_consumption_data']
    df_1 = dbRead(dbPath, tableNames[0])
    df_2 = dbRead(dbPath, tableNames[1])
    
    #generate dataframe containing summary table
    df_out = calcTBStats(df_1, df_2)

    #write new table using summary dataframe into a copy of db file that also contains summary table
    dbWrite(dbPath, 'load_summary', df_out)

    #plot load duration curves
    plotTables(df_1, df_2, tableNames)

#dbPath = "C:/Users/bgislas/Downloads/CSE_exercise_2021_09_29-13h_09m.db"
#DataProcessor(dbPath)
