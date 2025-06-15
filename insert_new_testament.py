
import json
import sqlite3

with open("bibliaAveMaria.json", "r", encoding="utf-8") as f:
    data = json.load(f)

old_testament = data["novoTestamento"]

conn = sqlite3.connect("bible.db")
cursor = conn.cursor()

for book in old_testament:
    book_name = book["nome"]
    author = "Desconhecido"

    for chapter in book["capitulos"]:
        chapter_number = chapter["capitulo"]

        for verse in chapter["versiculos"]:
            verse_number = verse["versiculo"]
            verse_text = verse["texto"]

            cursor.execute("""
                INSERT INTO verses (book, author, chapter, verse, text, is_new_testament)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (book_name, author, chapter_number, verse_number, verse_text, 1))

conn.commit()
conn.close()

print("new testament inserted")
