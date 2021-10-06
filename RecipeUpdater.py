import pandas as pd
import os

df = pd.DataFrame()
df = df.append(pd.read_excel('RecipeTable.xlsx'), ignore_index=True) 
df = df.iloc[:, 1:]
check = []

for i  in range(len(df)):
    if not df.iloc[i]['Site'] + df.iloc[i]['Line'] + df.iloc[i]['Equipment'] + df.iloc[i]['Recipe'] in check:
        check.append(df.iloc[i]['Site'] + df.iloc[i]['Line'] + df.iloc[i]['Equipment'] + df.iloc[i]['Recipe'])
        df2 = {'Site': df.iloc[i]['Site'], 'Line': df.iloc[i]['Line'], 
        'Equipment': df.iloc[i]['Equipment'], 'Recipe': df.iloc[i]['Recipe'], 'Datapoint': '00 - ProductID'}
        df = df.append(df2, ignore_index=True) 
       
print(df.shape)       
df.to_excel('NewRecipeTable.xlsx')