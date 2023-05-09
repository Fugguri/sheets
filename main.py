import gspread
import json
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


file = open("config.json", "r")
config = json.load(file)

TOKEN_API = config["TOKEN_API"]


storage = MemoryStorage()
bot = Bot(TOKEN_API, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)


async def on_startup(_):
    print("Бот запущен")


async def on_shutdown(_):
    print("Бот остановлен")


if __name__ == "__main__":

    from handlers import dp
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True
    )


def sheets_append_row(degree, phone, comment, feedback_data=None):
    # Указываем путь к JSON
    gc = gspread.service_account(
        filename='brave-design-383019-841912aaeec5.json')
    # Открываем тестовую таблицу
    sh = gc.open("degree")
    # print(sh)
    worksheet = sh.get_worksheet(0)

    values = ([degree, phone, comment, feedback_data])
    worksheet.append_row(values=values)
