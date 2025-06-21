import sqlite3

conn = sqlite3.connect("bible.db")
cursor = conn.cursor()

cursor.execute("ALTER TABLE verses ADD COLUMN abbrv TEXT")

conn.commit()
print("new column added")

book_abbrv = {
    "Gênesis": "Gn",
    "Êxodo": "Êx",
    "Levítico": "Lv",
    "Números": "Nm",
    "Deuteronômio": "Dt",
    "Josué": "Js",
    "Juízes": "Jz",
    "Rute": "Rt",
    "I Samuel": "1Sm",
    "II Samuel": "2Sm",
    "I Reis": "1Rs",
    "II Reis": "2Rs",
    "I Crônicas": "1Cr",
    "II Crônicas": "2Cr",
    "Esdras": "Ed",
    "Neemias": "Ne",
    "Tobias": "Tb",
    "Judite": "Jt",
    "Ester": "Et",
    "I Macabeus": "1Mc",
    "II Macabeus": "2Mc",
    "Jó": "Jó",
    "Salmos": "Sl",
    "Provérbios": "Pr",
    "Eclesiastes": "Ecl",
    "Cântico dos Cânticos": "Ct",
    "Sabedoria": "Sb",
    "Eclesiástico": "Eclo",
    "Isaías": "Is",
    "Jeremias": "Jr",
    "Lamentações": "Lm",
    "Baruc": "Br",
    "Ezequiel": "Ez",
    "Daniel": "Dn",
    "Oséias": "Os",
    "Joel": "Jl",
    "Amós": "Am",
    "Abdias": "Abd",
    "Jonas": "Jn",
    "Miquéias": "Mq",
    "Naum": "Na",
    "Habacuc": "Hc",
    "Sofonias": "Sf",
    "Ageu": "Ag",
    "Zacarias": "Zc",
    "Malaquias": "Ml",
    "São Mateus": "Mt",
    "São Marcos": "Mc",
    "São Lucas": "Lc",
    "São João": "Jo",
    "Atos dos Apóstolos": "At",
    "Romanos": "Rm",
    "I Coríntios": "1Cor",
    "II Coríntios": "2Cor",
    "Gálatas": "Gl",
    "Efésios": "Ef",
    "Filipenses": "Fp",
    "Colossenses": "Cl",
    "I Tessalonicenses": "1Ts",
    "II Tessalonicenses": "2Ts",
    "I Timóteo": "1Tm",
    "II Timóteo": "2Tm",
    "Tito": "Tt",
    "Filêmon": "Fm",
    "Hebreus": "Hb",
    "São Tiago": "Tg",
    "I São Pedro": "1Pd",
    "II São Pedro": "2Pd",
    "I São João": "1Jo",
    "II São João": "2Jo",
    "III São João": "3Jo",
    "São Judas": "Jd",
    "Apocalipse": "Ap"
}

for book, abbr in book_abbrv.items():
    cursor.execute(
        "UPDATE verses SET abbrv = ? WHERE book = ?", (abbr, book))

conn.commit()
conn.close()

print("Abbreviations updated.")
