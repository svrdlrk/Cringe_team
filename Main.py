import asyncio
import logging
import sys

import menu
import Inline_menu as imenu

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types import ReplyKeyboardRemove
from aiogram import F

# Токен бота
token = ''
bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"*Добрый день, {message.from_user.full_name}!*\nЭто бот с экскурсиями по Самаре.\n"
                         f"Здесь вы можете выбрать понравившуюся вам экскурсию и узнать ее стоимость",
                         reply_markup=imenu.menu, parse_mode="Markdown")


# @dp.callback_query(func=lambda c: c.data == 'choose_exc' )
# async def process_callback_choosebtn(callback_query: types.CallbackQuery):
#     await bot.answer_callback_query(callback_query.id)
#     await bot.send_message(callback_query.from_user.id, 'Вот экскурсии которые мы можем вам предложить')

@dp.message()
async def bot_msg(message: Message):
    if message.text == 'Выбор экскурсии:':
        await message.answer("На данный момент в боте предоставлены пять разных экскурсий:",
                             reply_markup=ReplyKeyboardRemove())
        await message.answer("Вы можете выбрать любую подходящую вам:", reply_markup=imenu.categories)
        # засунуть 5 экскурсий с превью и описанием ------ ГОТОВО
        # отредачить кнопки на телефоне по длине и размеру ------ ГОТОВО
    elif message.text == 'Поддержка':
        await message.answer("Если у вас возникли какие-то проблемы при пользовании нашим ботом или "
                             "у вас есть пожелания  по улучшению.\n Вы можете связаться с "
                             "нами по этому контакту @CheuChun", reply_markup=menu.menu)
    elif message.text == 'В начало':
        await message.answer(' ', reply_markup=menu.menu)
        # засунуть 10 сообщений на рандом ------ НЕГОТОВО


@dp.callback_query(F.data == 'choose_exc')
async def retun_to_start(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer('На данный момент в боте предоставлены пять разных экскурсий.\nВы можете выбрать '
                                  'любую подходящую вам:', reply_markup=imenu.categories)
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query(F.data == 'start')
async def retun_to_start(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(f"*Добрый день, {hbold(callback.from_user.full_name)}!*\nЭто бот с экскурсиями по "
                                  f"Самаре.\n"
                                  f"Здесь вы можете выбрать понравившуюся вам экскурсию и узнать ее стоимость",
                                  reply_markup=imenu.menu, parse_mode="Markdown")
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query(F.data == 'back')
async def retun_to_start(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("На данный момент в боте предоставлены пять разных экскурсий:",
                                  reply_markup=imenu.categories)
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query(F.data == 'exc1')
async def retun_to_start(callback: types.CallbackQuery):
    file_path = './Excursions/bars.jpg'
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(file_path),
                                        caption='*Тур "Исследование Баров Самары"*\n\nНаш тур предлагает погрузиться '
                                                'в богатство'
                                                'местных напитков и культуру города через его бары. От уютных пабов '
                                                'до стильных лаунджей, вы отправитесь в вкусовое путешествие, '
                                                'открывая для себя уникальные ароматы и впечатления, доступные лишь в '
                                                'этом уголке мира.',
                                        reply_markup=imenu.excursions, parse_mode="Markdown")
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query(F.data == 'exc2')
async def retun_to_start(callback: types.CallbackQuery):
    file_path = './Excursions/piter.jpg'
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(file_path),
                                        caption='*Тур "Питерские Зарисовки в Самаре"*\n\nДанный тур приглашает вас на '
                                                'захватывающее'
                                                'путешествие по архитектурным и культурным достопримечательностям, '
                                                'воссозданным в Самаре в стиле Петербурга. Вы погрузитесь в атмосферу '
                                                'северной столицы, исследуя узкие улочки, фасады зданий и другие '
                                                'интересные места, вдохновленные архитектурой Петербурга. Этот тур '
                                                'станет отличной возможностью познакомиться с уникальным сочетанием '
                                                'двух городов в одном.',
                                        reply_markup=imenu.excursions, parse_mode="Markdown")
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query(F.data == 'exc3')
async def retun_to_start(callback: types.CallbackQuery):
    await callback.answer()
    file_path = './Excursions/naba.jpg'
    await callback.message.answer_photo(photo=types.FSInputFile(file_path),
                                        caption='*Тур "Набережная Самары: По следам Волги"*\n\nЭтот тур позволит вам '
                                                'окунуться в'
                                                'уникальную атмосферу прибрежной зоны города, исследуя его историю, '
                                                'культуру и достопримечательности. Вы пройдете вдоль берега Волги, '
                                                'наслаждаясь красивыми видами, уютными кафе и интересными '
                                                'арт-объектами. Этот тур предоставит вам возможность узнать больше о '
                                                'жизни на реке и о том, как она влияет на городскую среду.',
                                        reply_markup=imenu.excursions, parse_mode="Markdown")
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query(F.data == 'exc4')
async def retun_to_start(callback: types.CallbackQuery):
    file_path = './Excursions/green.jpg'
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(file_path),
                                        caption='*Тур "Зеленые Уголки Самары"*\n\nДанный тур приглашает вас на '
                                                'экскурсию по самым'
                                                'живописным паркам города, где вы сможете насладиться природой и '
                                                'уютной атмосферой. Пройдясь по ухоженным аллеям и насладившись '
                                                'свежим воздухом, вы окунетесь в спокойную обстановку и забудете о '
                                                'городской суете. Этот тур подарит вам возможность расслабиться и '
                                                'насладиться прекрасными видами, которые предлагают парки Самары.',
                                        reply_markup=imenu.excursions, parse_mode="Markdown")
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


@dp.callback_query(F.data == 'exc5')
async def retun_to_start(callback: types.CallbackQuery):
    file_path = './Excursions/famous.jpg'
    await callback.answer()
    await callback.message.answer_photo(photo=types.FSInputFile(file_path),
                                        caption='*Тур "Самарская Визитная Карточка"*\n\nНаш тур предлагает '
                                                'погрузиться в мир'
                                                'главных достопримечательностей города. От исторических памятников до '
                                                'современных архитектурных шедевров, вы посетите самые узнаваемые '
                                                'места, оставляющие неповторимое впечатление о Самаре. Этот тур '
                                                'откроет перед вами красоту и уникальность города, '
                                                'оставляя незабываемые воспоминания о его культурном наследии.',
                                        reply_markup=imenu.excursions, parse_mode="Markdown")
    await bot.delete_message(chat_id=callback.from_user.id, message_id=callback.message.message_id)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
