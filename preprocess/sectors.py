import json
import os


os.chdir('/county_district')

county = ['新北市', 'NWT', '臺北市', 'TPE', '桃園市', 'TAO', '臺中市', 'TXG', '臺南市', 'TNN', '高雄市', 'KHH', '宜蘭縣', 'ILA', '新竹縣', 'HSQ', '苗栗縣', 'MIA', '彰化縣', 'CHA', '南投縣',
          'NAN', '雲林縣', 'YUN', '嘉義縣', 'CYQ', '屏東縣', 'PIF', '臺東縣', 'TTT', '花蓮縣', 'HUA', '澎湖縣', 'PEN', '基隆市', 'KEE', '新竹市', 'HSZ', '嘉義市', 'CYI', '金門縣', 'KIN', '連江縣', 'LIE']

for i in range(1, len(county)+1, 2):

    with open(county[i]+'.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    data_1 = []
    for i in data:
        data_1.append(i['計畫區代碼'])
        data_1.append(i['計畫區名稱'])

    print(data_1)
