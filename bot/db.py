import aiosqlite

DB_PATH = "database.db"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT,
            phone TEXT
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS cart (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            link TEXT,
            size TEXT,
            category TEXT,
            price REAL
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            user_id INTEGER,
            tracking TEXT,
            status TEXT,
            created_at TEXT
        )""")
        await db.execute("""CREATE TABLE IF NOT EXISTS order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT,
            link TEXT,
            size TEXT,
            category TEXT,
            price REAL
        )""")
        await db.commit()
