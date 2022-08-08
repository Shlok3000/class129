import csv

data = []
with open("dataset_2.csv", "r") as f:
    c = csv.reader(f)
    for i in c:
        data.append(i)

headers = data[0]
planet_data = data[1:]

for n in planet_data:
    n[2] = n[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("planet_data.csv", "a+") as p:
    h = csv.writer(p)
    h.writerow(headers)
    h.writerows(planet_data)