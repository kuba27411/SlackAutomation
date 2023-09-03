import requests
import json
import re


def send_json_payload(username, password):

    payload = {}

    auth = (username, password)

    response = requests.post("ENDPOINT", json=payload, auth=auth)

    json_response = json.loads(response.text)

    link_pattern = r"https://app-qa.trunarrative.cloud/ui/capture/[\w-]+"

    match = re.search(link_pattern, response.text)

    link = match.group() if match else None
    
    return link
