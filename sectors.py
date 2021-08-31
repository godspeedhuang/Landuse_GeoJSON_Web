import json

with open('TXG.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print(len(data))
data_1 = []
for i in data:
    data_1.append(i['計畫區代碼'])
    data_1.append(i['計畫區名稱'])

print(len(data_1))
