import asyncio
import requests
from pprint import pprint




from config import BOT_TOKEN

api_link = f"https://api.telegram.org/bot{BOT_TOKEN}"

updates = requests.get(api_link + "/getUpdates?offset=-1").json()

#pprint(updates)
message= updates['result'][0]['message']
chat_id =message['from']['id']
text = message['text']
print(chat_id, text)

for i in range(100):
    send_message = requests.get(api_link + f"/sendMessage?chat_id={chat_id}&text=Ты написал {text}?")