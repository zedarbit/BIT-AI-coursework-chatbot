import json
import logging

import requests

# user_massage = "你好鸭"
def dialog_with_pop(user_message):
    # message = "北理工有什么好玩的"
    message = user_message
    headers = {"Content-type": "application/json"}
    data = "{\"sender\": \"user\", \"message\":\" " + message + "\"}"
    response = requests.post("http://localhost:5005/webhooks/rest/webhook", headers=headers, data=data.encode())

    if json.loads(response.text):
        textResponse = json.loads(response.text)[0]["text"]
        print(textResponse)
        return textResponse

    else:
        logging.degug("an error happened")
