# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 15:19:38 2021

@author: Barbara
"""


import pandas as pd
import pyodbc


# Import CSV
data = pd.read_csv (r"/Users/Barbara/Desktop/Laboratory/ProgettoDati/data_cleaned/data_cleaned/tournament_cleaned.csv")   
df = pd.DataFrame(data)

#connect to data source, using userName and userPWD
server = 'lds.di.unipi.it' 
database = 'Group_14_DB' 
username = 'Group_14' 
password = '3L0YX720' 
connectionString = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

# Insert DataFrame to Table
for row in df.itertuples(index=False):
   cursor.execute("INSERT INTO Group_14.Tournament (tourney_id,tourney_date,tourney_name,surface,draw_size,tourney_level,tourney_spectators,tourney_revenue) values(?,?,?,?,?,?,?,?)", 
                  row.tourney_id, row.tourney_date, row.tourney_name, row.surface, row.draw_size, row.tourney_level, row.tourney_spectators, row.tourney_revenue)
conn.commit()
cursor.close()



