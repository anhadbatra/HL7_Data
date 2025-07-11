import requests
import json
import boto3

data = requests.get("https://hapi.fhir.org/baseR4/Patient?_count=10")

data = data.json()

print(data)