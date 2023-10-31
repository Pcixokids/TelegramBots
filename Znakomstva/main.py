

async def on_startup(dp):
    from data.config_sql import create_tables, default_insert
    await create_tables()
    await default_insert(dp)



if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    engine = db.create_engine('sqlite:///data/prod_sqlite.db')
    executor.start_polling(dp, on_startup=on_startup)

