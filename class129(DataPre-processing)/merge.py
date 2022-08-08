import csv
from textwrap import indent

dataset1 = []
dataset2 = []

with open("dataset_1.csv", "r") as t:
    a = csv.reader(t)
    for u in a:
        dataset1.append(u)

with open("planet_data.csv", 'r') as m:
    d = csv.reader(m)
    for y in d:
        dataset2.append(y)

header1 = dataset1[0]
header2 = dataset2[0]

planetdata1 = dataset1[1:]
planetdata2 = dataset2[1:]

headers = header1 + header2

planetdata = []

for index, item in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])

with open("final.csv", 'a+') as b:
    x = csv.writer(b)
    x.writerow(headers)
    x.writerows(planetdata)
