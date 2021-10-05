#import modules 
from ben_gislason_cse_exercise.utilities.db_read import dbRead
from ben_gislason_cse_exercise.utilities.db_open import openDb
from ben_gislason_cse_exercise.utilities.calc_tb_stats import calcTBStats
from ben_gislason_cse_exercise.utilities.db_write import dbWrite
from ben_gislason_cse_exercise.utilities.build_plots import plotTables
import os
import sqlite3

class DataProcessor:
    def __init__(self, db_path):
        """
        Open connection to database for downstream use
        """
        self.path = db_path
        self.conn = openDb(self.path)       

    def run_cse_exercise(self, path):
        """
        Create dataframes and generate plot and
        summary statistical table in copy of 
        database
        """
         #read data tables from SQLLite and convert to data frames for analysis
        tableNames = ['smaller_bin_consumption_data','larger_bin_consumption_data']
        
        df_1 = dbRead(self.conn, tableNames[0])
        df_2 = dbRead(self.conn, tableNames[1])

        #generate dataframe containing summary table
        df_out = calcTBStats(df_1, df_2)

        #write new table using summary dataframe into a copy of db file that also contains summary table
        path = dbWrite(self.path, 'load_summary', df_out)
        self.conn.close()

        #plot load duration curves
        plotTables(df_1, df_2, tableNames)
    
        return path
#my_data_processor = DataProcessor('c:/users/bgislas/Downloads/CSE_exercise_2021_09_29-13h_09m.db')
