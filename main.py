import requests
import time
import os
from keep_alive import keep_alive

keep_alive()

counter = 1  # Initialize the counter

def send_message():
    global counter  # Use the global counter variable
    payload = {
        'content': f"🤖 메시지 보냄 {counter} 🤖"  # Incrementing the number in the content field
    }

    headers = {
        'Authorization': os.environ.get('Token')
    }

    url = 'https://discord.com/api/v9/channels/1031505526669987930/messages'

    try:
        response = requests.post(url=url, data=payload, headers=headers)
        response.raise_for_status()
        print("메시지 전송 상태 코드:", response.status_code)
        print("메시지 전송 상태 : ", response.text)
        counter += 1  # Increment the counter after each successful message
    except requests.exceptions.RequestException as e:
        print("에러 발생:", e)

# Run the script every 1 second
while True:
    send_message()
    time.sleep(1)
