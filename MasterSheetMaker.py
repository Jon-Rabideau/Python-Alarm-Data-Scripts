import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
path_parent = os.path.abspath(os.curdir)
print(path_parent)
cwd = os.path.abspath('Excel Files/Master Files') 
files = os.listdir(cwd)
print(files)  


df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel('Excel Files/Master Files/' + file), ignore_index=True) 
df.head()
df = df.iloc[:, 1:-1]
print(df.shape)
for row in range(len(df)):
    if len(str(df.loc[row, 'description'])) > 100:
        print('##############################################################')
        print('WARNING! Description too long for ' + str(df.loc[row, 'system']) + 
        ' ' + str(df.loc[row, 'tag']) + ' ' + str(df.loc[row, 'number']))
        print('##############################################################') 
df.to_excel('Master_List.xlsx')
print('master updated')


################################
# Send table to database
################################

database_credentials = ('Driver={SQL Server};'
                        'Server=FO-CPS-PBI01;'
                        'Database=FairlifePackaging;'
                        'Trusted_Connection=yes;'
                        )

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": database_credentials})
engine = engine = create_engine(connection_url)

def replaceTable():
    while True:
        confirm = input('Would you like to replace Alarm Table? y/n\n')
        if confirm == 'y':
            df.to_sql('AlarmMapping_dim', con=engine, schema='ref', if_exists='replace')
            print('Please wait...')
            print('Table updated successfully')
            break
        elif confirm == 'n':
            break

replaceTable()