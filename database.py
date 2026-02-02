import sqlite3

def create_database():
    conn = sqlite3.connect("project.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS recommendations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT
    )
    """)

    conn.commit()
    conn.close()

