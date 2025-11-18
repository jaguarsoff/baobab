import sqlite3
import os

DB_PATH = "/app/data/database.db"

async def init_db():
    # Создаем директорию, если её нет
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        size TEXT,
        weight REAL,
        price REAL,
        total REAL,
        status TEXT DEFAULT 'new'
    )
    """)
    conn.commit()
    conn.close()

def new_order(user_id,link,size,category,qty,price,weight):
    conn=sqlite3.connect(DB_PATH); c=conn.cursor()
    c.execute("INSERT INTO orders(user_id,link,size,category,quantity,price,weight,status) VALUES(?,?,?,?,?,?,?,?)",
              (user_id,link,size,category,qty,price,weight,"created"))
    conn.commit(); conn.close()
