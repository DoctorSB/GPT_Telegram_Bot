#Сначала человек пишет основную информацию о себе, сколько ему лет, где он живет и мужчина он или женщина
#Далее он должен выбрать, какой язык он хочет изучать. На выбор немецкий и русский
#Человек должен выбрать, является ли он новичком или изучает язык
#Выбор города. Два варианта Брно или Прага
#Перед человеком будет описание подходящей языковой школы, а также будет вопрос, хочет ли он продолжить
# Если он согласен с условиями языковой школы, следующим шагом будет регистрация, где он напишете свои личные данные( имя фамилия и емейл). Когда он это сделает, появится уведомление, что ему скоро позвонят из школы.

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
choice = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text="Новичок", callback_data="newbie"),
                                        InlineKeyboardButton(text="Изучаю язык", callback_data="language")

                                    ],
                                    [
                                        InlineKeyboardButton(text="Мужчина", callback_data="man"),
                                        InlineKeyboardButton(text="Женщина", callback_data="woman")
                                    ],
                                    [
                                        InlineKeyboardButton(text="Немецкий", callback_data="german"),
                                        InlineKeyboardButton(text="Русский", callback_data="russian")
                                    ],
                                    [
                                        InlineKeyboardButton(text="Брно", callback_data="brno"),
                                        InlineKeyboardButton(text="Прага", callback_data="prague")

                                    ],
                                    [
                                        InlineKeyboardButton(text="Да", callback_data="yes"),
                                        InlineKeyboardButton(text="Нет", callback_data="no")

                                    ]
                                ]
                                )

