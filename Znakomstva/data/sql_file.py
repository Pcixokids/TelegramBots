import aiosqlite, traceback

path_to_db = 'data/bot_bd.sqlite'

async def create_table():
    async with aiosqlite.connect(path_to_db) as db:
        try:
            await db.execute("")
        except Exception as e:
            stack = traceback.extract_stack()
            print(f"An exception occured in {stack[-2][2]} | {e}")