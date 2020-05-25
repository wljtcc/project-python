#!/usr/bin/python3

from typing import List, Any
import requests
import datetime

dateTime = datetime.datetime.now()
url = []
currency_value = []
currency = ["bitcoin", "ethereum", "litecoin", "bitcoincash", "ripple", "eos"]
currency_list = ["BRLBTC", "BRLETH", "BRLLTC", "BRLBCH", "BRLXRP", "BRLEOS"]
length = len(currency)

dateTime = "Date | Time: " + str(dateTime.date().strftime("%d/%m/%y")) + " | " + str(dateTime.time().strftime("%H:%M:%S"))

def getCoins():
    for i in range(length):
        url.append(i)
        currency_value.append(i)
        url[i] = "https://api.bitcointrade.com.br/v3/public/" + currency_list[i] + "/ticker"
        currency_value[i] = requests.get(url[i])
        currency_value[i] = currency_value[i].json()

        for key, value in currency_value[i].items():
            json = value

        bot_message = str(currency[i]) + str(" --> R$ ") + str(json['last'])
        msg_return = botTelegram(bot_message)

def botTelegram(bot_message):
    # Configure Token
    bot_token = ''
    # Configure ChatBotID
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)
    return response.json()

# Send Date / Time
botTelegram(dateTime)
# Send Crypto Currency Values
getCoins()
botTelegram("=====================================")
