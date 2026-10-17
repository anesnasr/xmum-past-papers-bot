import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_code TEXT NOT NULL,
            year INTEGER NOT NULL,
            file_id TEXT NOT NULL,
            user_id INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def add_paper(course_code, year, file_id, user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO papers (course_code, year, file_id, user_id) VALUES (?, ?, ?, ?)",
        (course_code, year, file_id, user_id)
    )
    conn.commit()
    conn.close()