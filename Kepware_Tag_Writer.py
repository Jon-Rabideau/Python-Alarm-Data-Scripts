import os
import pandas as pd

master = pd.read_excel('Master_List.xlsx')
table = []

for i, row in master.iterrows():
    if 'Palletizer' in row.system:
        table.append(['PackagingPLCs.' + str(row.system) + '.' + str(row.tag) + '@Boolean', 
        str(row.system) + '.'+ str(row.tag)])
    elif 'CasePacker' in row.system:
        print
    elif 'Filler' in row.system:
        print
    elif 'Sleever' in row.system:
        print
    elif 'PalletWrapper' in row.system:
        table.append(['PackagingPLCs.' + str(row.system) + '.Global.' 
        + str(row.tag), str(row.system) + '.' + str(row.tag)])
    else:
        print('system not found')

df2 = pd.DataFrame(table)

fileName = 'TEST_Kepware_Tags.xlsx'
df2.to_excel(fileName)

