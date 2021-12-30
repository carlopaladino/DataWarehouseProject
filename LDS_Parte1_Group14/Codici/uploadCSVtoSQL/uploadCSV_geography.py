# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 18:24:05 2021

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
   cursor.execute("INSERT INTO Group_14.Geography (country_code,continent,language) values(?,?,?)", row.country_code, row.continent, row.language)

conn.commit()
cursor.close()