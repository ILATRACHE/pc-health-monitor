import requests
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
chat_id = os.getenv("CHAT_ID")

def send_message(message ):
    try : 
        url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {'chat_id':chat_id , 'text':message}
        respanse = requests.post(url , json=data)
        if respanse.status_code==200:
            print(f"alert sent : {message} ")
        else :
            print(f'Error : {respanse.text}')
    except requests.RequestException :
        pass

    
