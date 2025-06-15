import sqlite3

conn = sqlite3.connect("bible.db")
cursor = conn.cursor()
print("bible search")
print("1 - verse")
print("2 - books")
opt = input("option: ")
print("\n")

if opt == "1":
    book = input("book: ")
    chapter = int(input("chapter: "))
    verse = int(input("verse: "))
    cursor.execute("""
        SELECT text FROM verses
        WHERE book = ? AND chapter = ? AND verse = ?
        """, (book, chapter, verse,))
    rows = cursor.fetchall()

    for row in rows:
        text = row
        print(f"{book} {chapter}:{verse} - {text}")

if opt == "2":
    cursor.execute("SELECT DISTINCT book FROM verses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
conn.close()
