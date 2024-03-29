import sqlite3

def init_db():
    conn = sqlite3.connect('schedule.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, username TEXT, user_group TEXT)''')
    conn.commit()
    conn.close()

init_db()
