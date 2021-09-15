import os
import pandas as pd
cwd = os.path.abspath('Excel Files/In System') 
files = os.listdir(cwd)
print(files)  

## Method 1 gets the first sheet of a given file
df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel('Excel Files/In System/' + file), ignore_index=True) 
df.head()
df = df.iloc[:, 1:-1] 
df.to_excel('Master_List.xlsx')