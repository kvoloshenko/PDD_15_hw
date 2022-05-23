import  requests
import pprint
import time

#https://core.telegram.org/bots/api

token = 'MY_TOKEN'

# Чтение файла
with open('token', 'r') as f:
    # 1. Прочитать сразу все данные
    token = f.read()
    # print(token)

MAIN_URL = f'https://api.telegram.org/bot{token}'

# Информация о боте
url = f'{MAIN_URL}/getMe'

print(url)
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}
result = requests.get(url, headers=headers)

pprint.pprint(result.json())

# Обновления
msg_received = False
while not msg_received:
    time.sleep(15)
    url = f'{MAIN_URL}/getUpdates'

    result = requests.get(url, headers=headers)

    pprint.pprint(result.json())

    messages = result.json()['result']

    for message in messages:
        # Как ответить на сообщение
        chat_id = message['message']['chat']['id']
        url = f'{MAIN_URL}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': 'Привет User!'
        }

        result = requests.post(url, headers=headers, params=params)
        pprint.pprint(result.json())
        msg_received = True