import requests
import json

data = requests.get("https://hapi.fhir.org/baseR4/Patient?_count=10")

data = data.json()

print(data)