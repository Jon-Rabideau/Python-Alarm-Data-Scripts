import re
import pandas as pd
count = 0
index = []
type = []
message = []
table = [['tag', 'system', 'number', 'description']]
pre = "<![CDATA['"
post = "']]>"
# openFile is txt to import, saveFile is excel to export
openFile = 'Text Files\L1_CasePacker_Filtered_P0System.txt'
saveFile = 'L1_CasePacker_P0System_Alarm_Data.xlsx'
currentTag = 'P0System_AlarmNo'
currentSystem = 'L1_CasePacker'

# Open file
with open(openFile) as file:
    print('file open')
    for line in file:

        # Search for first brackets (index)
        indexResult = re.search(r"\[([A-Za-z0-9_]+)\]", line)
        if indexResult:
            index.append(indexResult.group(1))

        # Search for other brackets (message info)
        messageResult = re.search(r"<!\[CDATA\[[^\]]*]]>", line)
        if messageResult:
            if count == 0:
                typeTemp = messageResult.group().replace(pre, '').replace(post, '')
                if typeTemp == '<![CDATA[]]>':
                    typeTemp = 'NA'
                type.append(typeTemp)
                count += 1
            else:
                messageTemp = messageResult.group().replace(pre, '').replace(post, '')
                if messageTemp == '<![CDATA[]]>':
                    messageTemp = ''
                message.append(messageTemp)
                count = 0


file.close()

# Create table from data collected 
for i in range(len(index)):
    table.append([currentTag, currentSystem, index[i], type[i] + ' ' + message[i]])

df = pd.DataFrame(table)
print(df)
fileName = saveFile
df.to_excel(fileName, header=False)

print('done')
# print(table)
