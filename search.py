import sqlite3

# Conectar ao banco
conn = sqlite3.connect("bible.db")
cursor = conn.cursor()
book = input("Livro: ")

# Executar a consulta (exemplo: versículos do livro de Gênesis)
cursor.execute(
    "SELECT book, chapter, verse, text FROM verses WHERE book = ?", (book,))

# Buscar os resultados
rows = cursor.fetchall()

# Iterar e imprimir
for row in rows:
    book, chapter, verse, text = row
    print(f"{book} {chapter}:{verse} - {text}")

# Fechar conexão
conn.close()
