import requests
import json
import numpy as np

url = "http://127.0.0.1:8000/my_app/api/my_app/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)


data = json.loads(response.text)
x = []
for val in data:
    x.append(val['salary'])
print(x)

y = np.array(x)
z = np.average(y)
print(z)

for emp in data:
    if emp['hire_date'] < '2021-03-20' and emp['salary'] < z:
        with open("poor_employees.txt", "a+") as file:
            file.write(str(emp)+"\n\n")














