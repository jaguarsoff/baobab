import random
from datetime import datetime
from bot.config import settings

def gen_order_uid():
    return str(random.randint(100000, 999999))

def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M')
