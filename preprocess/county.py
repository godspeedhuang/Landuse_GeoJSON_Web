import pandas as pd

df = pd.read_csv('taiwan_administrative_divisions.csv')
df
data = []

for i in range(22):
    data.append(list(df.iloc[i, [5, 1]]))


print(data)

datas = []
for i in data:
    for j in i:
        datas.append(j)
print(datas)
