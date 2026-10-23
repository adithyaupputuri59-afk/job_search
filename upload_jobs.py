
import pandas as pd
import requests

df = pd.read_excel("jobs.xlsx")
jobs = df.to_dict(orient="records")

url = "http://127.0.0.1:8000/api/jobs/"

response = requests.post(url, json=jobs, auth=("your_username", "your_password"))

print("Status code:", response.status_code)
print(response.text)
