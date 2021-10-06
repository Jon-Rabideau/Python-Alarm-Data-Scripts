import pandas
# import csv file
df = pandas.read_csv('L6_BEMA_FairLife_17CC059_8SEPT2020-Tags.CSV', header=6, encoding='latin1')
# filter out alarm data, save to new df

df2 = df[(df['NAME'] == ('ALARM')) & (df['DESCRIPTION'].notnull())].reset_index()
df2 = df2[df2['SPECIFIER'].str.contains('ALARM')].reset_index()
print(df2['SPECIFIER'])

# create alarm no cloumn based on index
df2['number'] = df2.index
df2['system'] = 'L6_Palletizer'
df2['tag'] = df2.SPECIFIER
df2['description'] = df2.DESCRIPTION
df2 = df2[['tag','system','number','description']]

# cast to str, remove bracketed alarm info and other unwanted chars, ex "[146] Open Flap" to "Open Flap"
df2 = df2.astype(str)

for i, row in df2.iterrows():
    if 'Alarms.DINT' not in df2.tag:
        row.drop
    row.description = row.description.replace('$N', ' ')
    row.description = row.description.replace('$', '')
    if isinstance(row.description, str) and row.description.find('[') == 0:
        row.description = row.description[row.description.find(']') + 2 :]
        
# save to excel file
file_name = 'Excel files/L6_Palletizer_Alarm_Data.xlsx'
df2.to_excel(file_name)
