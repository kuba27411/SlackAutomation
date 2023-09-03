Slack Automation
This repository contains a Python program for automating tasks related to Slack using the Slack API. The program consists of two main components: apiHandler and slackHandler.

Project Structure
The project has the following folder structure:

SLACKAUTOMATION
SRC
apiHandler
apiHandler.py: Python script for handling API requests and sending messages to Slack channels.
slackHandler
slack.py: Python script for interacting with the Slack API.
BAT.RUN: Batch file for running the program.
Setup
To set up and run the program, follow these steps:

Clone the repository to your local machine or download the source code.

Install the required dependencies by running the following command:

Copy code
pip install slack_sdk pandas
Make sure you have a valid Slack API token. If not, obtain one by creating a new Slack app and generating a token with the necessary permissions.

Update the API token in the YOUR_SLACK_TOKEN with your actual token.

Run the program by executing the BAT.RUN file or by running the apiHandler.py script directly.

Functionality
The program automates the process of sending messages to Slack channels using the Slack API. It fetches user IDs from an Excel file (user_ids.xlsx) located in the SRC directory.

The apiHandler component handles API requests and message sending. It imports the slackHandler module and uses the send_json_payload function from slack.py to send messages.

The slackHandler component contains the slack.py script, which provides functions for interacting with the Slack API.

Please ensure that you have the necessary permissions and valid inputs (such as user IDs in the Excel file) for the program to function correctly.

Feel free to explore the code and customize it according to your specific requirements.

Feel free to adjust and customize the README file based on your preferences and specific details of your project.
