import sqlalchemy as db
from aiogram import types
from main import engine

async def insert_in_table_registration(user_id, name, age, city, photo, username, sex, description, target):
    #engine = db.create_engine('sqlite:///data/prod_sqlite.db')
    metadata = db.MetaData()
    start_reg = db.Table("registration", metadata, autoload_with=engine)
    print(start_reg.columns)
    #print(metadata)
    #print(start_reg)
    connection = engine.connect()
    insert = start_reg.insert().values(id=user_id, name=name, age=age, city=city, photo=photo, nametg=username, sex=sex, description=description, target=target)
    connection.execute(insert)

async def default_insert(dp):
    print('Bot started')
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота")
    ])

async def create_tables():

    #engine = db.create_engine('sqlite:///data/prod_sqlite.db')

    #connection = engine.connect()

    metadata = db.MetaData()

    start_reg = db.Table("registration", metadata,
                        db.Column("id", db.Integer),
                        db.Column("name", db.Text),
                        db.Column("age", db.Integer),
                        db.Column("city", db.Text),
                        db.Column("photo", db.Text),
                        db.Column("nametg", db.Text),
                        db.Column("sex", db.Text),
                        db.Column("description", db.Text),
                        db.Column("target", db.Text),
                        )

    metadata.create_all(engine)