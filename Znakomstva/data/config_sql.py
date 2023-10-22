import sqlalchemy as db
from aiogram import types

async def default_insert(dp):
    print('Bot started')
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота")
    ])

async def create_tables():

    engine = db.create_engine('sqlite:///data/prod_sqlite.db')

    connection = engine.connect()

    metadata = db.MetaData()

    products = db.Table("registration", metadata,
                        db.Column("ID", db.Integer, primary_key=True),
                        db.Column("Name", db.Text),
                        db.Column("Age", db.Integer),
                        db.Column("City", db.Text),
                        db.Column("Photo/Video", db.Text),
                        db.Column("NameTG", db.Text),
                        db.Column("Male/Female", db.Text),
                        db.Column("Description", db.Text)
                        )

    metadata.create_all(engine)