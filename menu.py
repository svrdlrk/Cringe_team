from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ----Первая страница----
btnMenu = KeyboardButton(text='Выбор экскурсии:')
btnHelp = KeyboardButton(text='Поддержка')
menu = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btnMenu], [btnHelp]])

btnMain = KeyboardButton(text='В начало')
# ----Список категорий----
btnFirstCat = KeyboardButton(text='Первая категория')
btnSecondCat = KeyboardButton(text='Вторая категория')
btnThirdCat = KeyboardButton(text='Третья категория')
btnFourthCat = KeyboardButton(text='Четвертая категория')
btnFifthCat = KeyboardButton(text='Пятая категория')
categories = ReplyKeyboardMarkup(resize_keyboard=True,
                                 keyboard=[[btnFirstCat, btnSecondCat, btnThirdCat, btnFourthCat, btnMain]])
