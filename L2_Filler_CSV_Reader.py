import pandas
# import csv file
df = pandas.read_csv('Filler_L3_P14207_08JAN20-Tags.CSV', header=6, encoding='latin1')
# filter out alarm data, save to new df
df2 = df[(df['NAME'] == ('FIL_Event')) & df['DESCRIPTION'].notnull()].reset_index()

# create alarm no cloumn based on index
df2['number'] = df2.index
df2['system'] = 'L2_Filler'
df2['tag'] = df2.SPECIFIER
df2['description'] = df2.DESCRIPTION
df2 = df2[['tag','system','number','description']]

# cast to str, remove bracketed alarm info and other unwanted chars, ex "[146] Open Flap" to "Open Flap"
df2 = df2.astype(str)

for i, row in df2.iterrows():
    row.description = row.description.replace('$N', ' ')
    row.description = row.description.replace('$', '')
    if isinstance(row.description, str) and row.description.find('[') == 0:
        row.description = row.description[row.description.find(']') + 2 :]
        
# save to excel file
file_name = 'Excel files/L3_Filler_Alarm_Data.xlsx'
df2.to_excel(file_name)
