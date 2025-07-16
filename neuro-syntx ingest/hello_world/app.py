import requests
import json
import boto3
import datetime


s3_bucket = "neurosytnx-raw"
s3 = boto3.client('s3')
FHIR_API = "https://hapi.fhir.org/baseR4/Patient?_count=10"

def lambda_handler(event,context):
    data = requests.get(FHIR_API)
    data = data.json()
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    s3_key = f"fhir_data/patients_{timestamp}.json"

    s3.put_objects(
        BUCKET = s3_bucket,
        KEY = s3_key,
        Body = json.dumps(data),
        ContentType = "application/json"
    )


