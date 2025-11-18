import aiosqlite
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / 'poizon_v2.db'

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS cart(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            link TEXT,
            size TEXT,
            category TEXT,
            price_yuan REAL
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_uid TEXT UNIQUE,
            user_id INTEGER,
            total_rub REAL,
            status TEXT,
            tracking TEXT,
            created_at TEXT
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS order_items(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            link TEXT,
            size TEXT,
            category TEXT,
            price_yuan REAL
        )""")
        await db.commit()
