# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:40:14 2021

@author: Barbara
"""


import pandas as pd
import pyodbc


# Import CSV
data = pd.read_csv (r"/Users/Barbara/Desktop/Laboratory/ProgettoDati/data_cleaned/data_cleaned/date_cleaned.csv")   
df = pd.DataFrame(data)

#connect to data source, using userName and userPWD
server = 'lds.di.unipi.it' 
database = 'Group_14_DB' 
username = 'Group_14' 
password = '3L0YX720' 
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

for row in df.itertuples(index=False):
   cursor.execute("INSERT INTO Group_14.Match (tourney_id,match_id,winner_id,loser_id,score,best_of,round,winner_rank,winner_rank_points,loser_rank,loser_rank_points) values(?,?,?,?,?,?,?,?,?,?,?)",
                  row.tourney_id, row.match_id, row.winner_id, row.loser_id, row.score, row.best_of, row.round, row.winner_rank, row.winner_rank_points, row.loser_rank, row.loser_rank_points )

conn.commit()
cursor.close()

