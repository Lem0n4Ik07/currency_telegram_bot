#------------------------------------- импорт модулей -------------------------------------#

import config
import logging
import logging
import re

from aiogram import Bot, Dispatcher, executor, types

from pycbrf import ExchangeRates
from datetime import datetime


logging.basicConfig(level=logging.INFO)

#--------------------------------------- токен бота ---------------------------------------#

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#--------------------------------------- курс валют ---------------------------------------#

rates = ExchangeRates(str(datetime.now())[:10])

USD = round(rates['USD'].rate, 1)
EUR = round(rates['EUR'].rate, 1)
BYN = round(rates['BYN'].rate, 1)
KZT = round(rates['KZT'].rate, 1)


course = f"🇺🇸 USD - {USD} \n" f"🇪🇺 EUR - {EUR} \n" f"🇧🇾 BYN - {BYN} \n" f"🇰🇿 KZT - {KZT} \n"


@dp.message_handler()
async def currency(message: types.message):
    if "КУРС" in message.text:
        await message.answer(course)


#------------------------------------------ рубли -----------------------------------------#

    # Проверяем, что сообщение содержит числа
    Number_Rubles = r'\b\d+(?:\.\d+)?(?:\s{0,1})(?:р|руб|рублей|рэ|рубликов|Р|Руб|Рублей|Рэ|Рубликов|U+20BD)\b'

    Match_Rubles = re.search(Number_Rubles, message.text.lower())

    if Match_Rubles:

        Result = str(Match_Rubles.group())

        Result = int(re.sub("\D", " ", Result))


        Result_USD = (round(Result / USD, 1))
        Result_EUR = (round(Result / EUR, 1))
        Result_BYN = (round(Result / BYN, 1))
        Result_KZT = (round(Result / KZT, 1))

        await message.reply(f"🇺🇸 USD - {Result_USD} \n" f"🇪🇺 EUR - {Result_EUR} \n" f"🇧🇾 BYN - {Result_BYN} \n" f"🇰🇿 KZT - {Result_KZT} \n")


#----------------------------------------- тысячи -----------------------------------------#

    # Проверяем, что сообщение содержит числа
    Number_Thousands = r'\b\d+(?:\.\d+)?(?:\s{0,1})(?:тыс|тысяч|т|Т|Тысяч|Тыс|к|ка)\b'

    Match_Thousands = re.search(Number_Thousands, message.text.lower())

    if Match_Thousands:

        Result = str(Match_Thousands.group())

        Result = int(re.sub("\D", " ", Result))


        Result_USD = (round(Result * 1000 / USD, 1))
        Result_EUR = (round(Result * 1000 / EUR, 1))
        Result_BYN = (round(Result * 1000 / BYN, 1))
        Result_KZT = (round(Result * 1000 / KZT, 1))

        await message.reply(f"🇺🇸 USD - {Result_USD} \n" f"🇪🇺 EUR - {Result_EUR} \n" f"🇧🇾 BYN - {Result_BYN} \n" f"🇰🇿 KZT - {Result_KZT} \n")


#----------------------------------------- доллары ----------------------------------------#

    # Проверяем, что сообщение содержит числа
    Number_Dollars = r'\b\d+(?:\.\d+)?(?:\s{0,1})(?:долларов|бакс|доллар|баксов|бакса)\b'

    Match_Dollars = re.search(Number_Dollars, message.text.lower())

    if Match_Dollars:

        Result = str(Match_Dollars.group())

        Result = int(re.sub("\D", " ", Result))


        Result_RUB = (round(Result * USD, 1))
        Result_EUR = (round(Result_RUB / EUR, 1))
        Result_BYN = (round(Result_RUB / BYN, 1))
        Result_KZT = (round(Result_RUB / KZT, 1))

        await message.reply(f"🇷🇺 RUB - {Result_RUB} \n" f"🇪🇺 EUR - {Result_EUR} \n" f"🇧🇾 BYN - {Result_BYN} \n" f"🇰🇿 KZT - {Result_KZT} \n")





#--------------------------------------- Запуск бота --------------------------------------#
if __name__ == "__main__":
    executor.start_polling(dp)
