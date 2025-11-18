Poizon AIogram Bot
==================

This project is a full-featured Poizon ordering bot built with aiogram 3.x.

Features:
- Menu-driven navigation
- Cart (add/remove/list)
- Order checkout with contact storage
- Price calculation (CNY->RUB) with delivery & fees
- Admin panel: list orders, change status, notify users
- Notifications on status change
- SQLite storage with aiosqlite
- FSM for guided flows

Run:
1. pip3 install -r requirements.txt
2. Fill .env with BOT_TOKEN and ADMIN_IDS
3. python3 main.py
