import sqlite3

conn = sqlite3.connect("bible.db")
cursor = conn.cursor()
print("bible search")
print("1 - verse")
print("2 - books")
print("3 - chapter")

opt = input("option: ")

print("\n")

if opt == "1":
    book = input("Abbreviation: ")
    chapter = int(input("chapter: "))
    verse_begin = int(input("verse begin: "))
    verse_end = int(input("verse end: "))
    cursor.execute("""
        SELECT text FROM verses
        WHERE abbrv = ? AND chapter = ? AND verse BETWEEN ? AND ?
        """, (book, chapter, verse_begin, verse_end,))
    rows = cursor.fetchall()

    for row in rows:
        text = row
        print(f"{text}")

if opt == "2":
    cursor.execute("SELECT DISTINCT book, abbrv FROM verses")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if opt == "3":
    book = input("Abbreviation: ")
    chapter = input("chapter: ")
    cursor.execute(
        "SELECT text FROM verses WHERE abbrv = ? AND chapter = ?", (book, chapter,))
    rows = cursor.fetchall()

    for row in rows:
        i = 1
        print(f"{i}:{row}")

conn.close()
