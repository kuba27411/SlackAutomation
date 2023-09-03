from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import pandas as pd
from slack import send_json_payload



def generate_and_send_links():
    slack_token = "Your_Slack_Token"
    slack_client = WebClient(token=slack_token)

    username = "AuthUsername"
    password = "AuthPassword"

    df = pd.read_excel("C:/Users/Jakub/Desktop/SlackAutomation/src/user_ids.xlsx")
    user_ids = df['User ID'].tolist()

    for user_id in user_ids:
        link = send_json_payload(username, password)
        message = f"This is your link to test Guided Capture: {link}"

        try:
            response = slack_client.conversations_open(users=[user_id])
            channel_id = response["channel"]["id"]

            response = slack_client.chat_postMessage(channel=channel_id, text=message)
            print(f"Message sent to {user_id} successfully!")
        except SlackApiError as e:
            print(f"Error sending message to {user_id}: {e.response['error']}")

generate_and_send_links()
