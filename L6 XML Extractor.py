import re
import pandas as pd
count = 0
check = False
index = []
type = []
message = []
table = [['tag', 'system', 'number', 'description']]
pre = "<![CDATA['"
post = "']]>"
# openFile is txt to import, saveFile is excel to export
openFile = 'TEXT_L6_Casepacker_SystemMsg.txt'
saveFile = 'L6_CasePacker_System_Alarm_Data.xlsx'
currentTag = 'Metering_AlarmNo'
currentSystem = 'L6_CasePacker'

# Open file
with open(openFile) as file:
    print('file open')
    for line in file:

        # Search for first brackets (index)
        indexResult = re.search(r"\[([A-Za-z0-9_]+)\]", line)
        if indexResult and check and indexResult.group(1) != '0':
            index.append(indexResult.group(1))

        # Search for other brackets (message info)
        messageResult = re.search(r"<!\[CDATA\[[^\]]*]]>", line)
        if messageResult:
            if check == False:
                check = True
            if count == 0:
                messageTemp = messageResult.group().replace(pre, '').replace(post, '')
                if messageTemp == '<![CDATA[]]>':
                    messageTemp = 'remove'
                    message.append(messageTemp)
                else:
                    message.append(messageTemp)
                count += 1
            elif count == 1:
                count += 1
            else:
                count = 0


file.close()

# Create table from data collected 
for i in range(len(index)):
    if message[i] != 'remove':
        table.append([currentTag, currentSystem, index[i], message[i]])

df = pd.DataFrame(table)
fileName = saveFile
df.to_excel(fileName, header=False)

print('done')
# print(table)
