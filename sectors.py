import json

with open('TXG.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


data_1 = []
for i in data:
    data_1.append(i['計畫區名稱'])

print(data_1)
