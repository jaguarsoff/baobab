
import sqlite3

DB_PATH = "/mnt/data/poizon.sqlite"

async def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS orders(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        link TEXT,
        size TEXT,
        category TEXT,
        quantity INTEGER,
        price REAL,
        weight REAL,
        status TEXT
    );""")
    c.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        phone TEXT,
        name TEXT
    );""")
    conn.commit(); conn.close()

def new_order(user_id,link,size,category,qty,price,weight):
    conn=sqlite3.connect(DB_PATH); c=conn.cursor()
    c.execute("INSERT INTO orders(user_id,link,size,category,quantity,price,weight,status) VALUES(?,?,?,?,?,?,?,?)",
              (user_id,link,size,category,qty,price,weight,"created"))
    conn.commit(); conn.close()
