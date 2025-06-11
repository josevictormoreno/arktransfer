import sqlite3

conn = sqlite3.connect("bible.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS verses")

cursor.execute("""
CREATE TABLE IF NOT EXISTS verses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book TEXT NOT NULL,
    author TEXT,
    chapter INTEGER NOT NULL,
    verse INTEGER NOT NULL,
    text TEXT NOT NULL,
    is_new_testament BOOLEAN NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and table created.")
