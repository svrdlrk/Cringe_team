from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ----Первая страница----
btnMenu = InlineKeyboardButton(text='Выбор экскурсии:', callback_data='choose_exc')
btnHelp = InlineKeyboardButton(text='Поддержка', callback_data='help')
menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[[btnMenu],[btnHelp]])

btnMain = InlineKeyboardButton(text='В начало', callback_data= 'start')

# ----Список категорий----
btnFirstCat = InlineKeyboardButton(text='Тур по Барам', callback_data='exc1')
btnSecondCat = InlineKeyboardButton(text='Архитектура Санкт-Петербурга', callback_data='exc2')
btnThirdCat = InlineKeyboardButton(text='По следам Волги', callback_data='exc3')
btnFourthCat = InlineKeyboardButton(text='Зеленые уголки Самары', callback_data='exc4')
btnFifthCat = InlineKeyboardButton(text='Самарская визитная карточка', callback_data='exc5')
categories = InlineKeyboardMarkup(row_width=1, inline_keyboard=[
    [btnFirstCat], [btnSecondCat], [btnThirdCat], [btnFourthCat], [btnFifthCat], [btnMain]])

# ----Экскурсии----
btnWant = InlineKeyboardButton(text='Хочу:', callback_data='want')
btnBack = InlineKeyboardButton(text='Назад:', callback_data='back')
excursions = InlineKeyboardMarkup(row_width=1,inline_keyboard=[[btnWant],[btnBack]])
