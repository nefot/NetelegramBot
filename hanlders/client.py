from loader import bot, dp
from aiogram.types import Message, InputFile, ReplyKeyboardRemove, CallbackQuery
from keybroa import keybroaddd, inline

switch_status = True


@dp.message_handler(commands=['start', 'help'])
async def command_star(message: Message):
    await message.reply(text='привет, медвед')
    # await message.answer(text='привет, медвед')
    # await bot.send_message(message.from_user.id, text='привет, медвед')
    await bot.send_message(message.from_user.id, text='ghbrrf', reply_markup=keybroaddd.menu)


@dp.message_handler(commands=['лампочка', 'Лампочка'])
async def command_light(message: Message):
    global switch_status
    if switch_status:
        await message.answer(text='выключенно')
        img = InputFile("media/img/light_bulb_off.png")
    else:
        await message.answer(text='включенно')
        img = InputFile("media/img/light_bulb_on.png")

    await bot.send_photo(message.migrate_from_chat_id, img, reply_markup=ReplyKeyboardRemove())
    switch_status = not switch_status


@dp.message_handler(commands=['/tv socket'])
async def command_tv(message: Message):
    await message.answer("Что сделать?", reply_markup=inline.inkb)


@dp.callback_query_handler(text='/tv socket')
async def command_1(callback: CallbackQuery):
    await callback.answer("Тв выключенно")
