import json
import csv
import pandas as pd

st = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

# pandas
df = pd.read_csv('data.csv')
print(df)


# CSV文件
# with open('data.csv', 'w') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow(({'id': '10001', 'name': 'Mike', 'age': 20}))
#     writer.writerow(({'id': '10002', 'name': 'Bob', 'age': 22}))
#     writer.writerow(({'id': '10003', 'name': 'Jordan', 'age': 21}))
#     # writer = csv.writer(csvfile, delimiter=' ')
#     # writer = csv.writer(csvfile)
#     # writer.writerow(['id', 'name', 'age'])
#     # writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
#     # writer.writerow(['10001', 'Mike', 20])
#     # writer.writerow(['10002', 'Bob', 22])
#     # writer.writerow(['10003', 'Jordan', 21])
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


# with open('data.json', 'r', encoding='utf-8') as file:
#     st = file.read()
#     data = json.loads(st)
#     print(data)
# with open('data2.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(data, indent=2, ensure_ascii=False))


# json.loads()
# print(type(st))
# data = json.loads(st)
# print(data)
# print(type(data))
# print(data[0]['name'])
# print(data[0].get('name'))
# print(data[0].get('age'))
# print(data[0].get('age', '123'))
