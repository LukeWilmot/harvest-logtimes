import os
import json
import urllib.request

url = "https://api.harvestapp.com/v2/time_entries"
headers = {
    "User-Agent": "Python Harvest API Sample",
    "Authorization": "Bearer " + os.environ.get("HARVEST_ACCESS_TOKEN"),
    "Harvest-Account-ID": os.environ.get("HARVEST_ACCOUNT_ID")
}

def lambda_handler(event, context):
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request, timeout=5)
    responseBody = response.read().decode("utf-8")
    jsonResponse = json.loads(responseBody)

    print(json.dumps(jsonResponse, sort_keys=True, indent=4))
