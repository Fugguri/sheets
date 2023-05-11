from aiogram import types
from main import dp
from aiogram.dispatcher.filters.state import State, StatesGroup
# from .google import google_sheet_update
import gspread


class Add(StatesGroup):
    add = State()


kb = types.InlineKeyboardMarkup()
kb.add(types.InlineKeyboardButton(text="Add new data", callback_data="add"))


async def google_sheet_update(*args):
    # Указываем путь к JSON
    gc = gspread.service_account(
        filename='brave-design-383019-841912aaeec5.json')
    # Открываем тестовую таблицу
    sh = gc.open("LAND tg")
    # print(sh)
    worksheet = sh.get_worksheet(0)

    values = (args)

    worksheet.append_row(values=values)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("""Wellcome.\nPlease send message using this template.\n
1. Date:
2. Location:
3. Ha/Are:
4. Price:
5. Zone:
6. Link:
""", reply_markup=kb)


@dp.message_handler(state=Add.add)
async def start(message: types.Message):
    try:
        data = message.text.split("\n")
        Date = data[0].replace("1. Date:", "").strip()
        Location = data[1].replace("2. Location:", "").strip()
        Are = data[2].replace("3. Ha/Are:", "").strip()
        Price = data[3].replace("4. Price:", "").strip()
        Zone = data[4].replace("5. Zone:", "").strip()
        Link = data[5].replace("6. Link:", "").strip()

        await google_sheet_update(Date, Location, Are, Price, Zone, Link)
        await message.answer(f"""<b>Succes!!!</b>\nPlease send message using this template.\n
1. Date:{Date}
2. Location:{Location}
3. Ha/Are:{Are}
4. Price:{Price}
5. Zone:{Zone}
6. Link:{Link}
""", reply_markup=kb)
    except:
        await message.answer(f"""<b>Error</b>\nplease try again""", reply_markup=kb)


@dp.callback_query_handler(lambda call: call.data == "add")
async def start(callback: types.CallbackQuery):
    await Add.add.set()
    await callback.message.answer(text="""\nPlease send message using <b>this</b> template.\n""")
    await callback.message.answer(text="""1. Date:
2. Location:
3. Ha/Are:
4. Price:
5. Zone:
6. Link:
""",)


@dp.message_handler()
async def start(message: types.Message):
    if "1. Date:" in message.text:
        try:
            data = message.text.split("\n")
            Date = data[0].replace("1. Date:", "").strip()
            Location = data[1].replace("2. Location:", "").strip()
            Are = data[2].replace("3. Ha/Are:", "").strip()
            Price = data[3].replace("4. Price:", "").strip()
            Zone = data[4].replace("5. Zone:", "").strip()
            Link = data[5].replace("6. Link:", "").strip()

            await google_sheet_update(Date, Location, Are, Price, Zone, Link)
            await message.answer(f"""<b>Succes!!!</b>\nPlease send message using this template.\n
1. Date:{Date}
2. Location:{Location}
3. Ha/Are:{Are}
4. Price:{Price}
5. Zone:{Zone}
6. Link:{Link}
""", reply_markup=kb)
        except:
            await message.answer(f"""<b>Error</b>\nplease try again""", reply_markup=kb)
