import requests

TOKEN = '999602825:AAFLxnk1nvT3zZY-ZCuZIeSLMoAqOVwZnh4'
MAIN_URL = f'https://api.telegram.org/bot{TOKEN}'

payload = {
    'chat_id': 37922243,
    'text': 'Привет',
    'reply_to_message_id':2
}
r = requests.get(f'{MAIN_URL}/sendMessage', data=payload)


print(r.json())