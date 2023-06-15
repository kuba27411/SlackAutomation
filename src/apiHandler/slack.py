import requests
import json
import re


def send_json_payload(username, password):

    payload = {
        "accountStrategyId": 347,
        "accountreference": "",
        "application": {
            "country": "GBR",
            "clientApplicationPurpose": ""
        },
        "person": [
            {
                "isPrimary": True,
                "role": "APPLICANT",
                "clientReference": "{{$isoTimestamp}}",
                "firstName": "Hello",
                "lastName": "Player-One"
            }
        ]
    }

    auth = (username, password)

    response = requests.post("https://qa.trunarrative.cloud/TruAccountAPI/rest/Accounts/v1/RunStrategy", json=payload, auth=auth)

    json_response = json.loads(response.text)

    link_pattern = r"https://app-qa.trunarrative.cloud/ui/capture/[\w-]+"

    match = re.search(link_pattern, response.text)

    link = match.group() if match else None
    
    return link