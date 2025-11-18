import random
from datetime import datetime

def generate_order_id():
    return str(random.randint(100000, 999999))

def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M')
