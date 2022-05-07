from loader import dp

if __name__ == '__main__':
    from aiogram import executor
    from hanlders.admin import on_start

    executor.start_polling(dp, on_startup=on_start, skip_updates=True)
