import sqlite3

conn = sqlite3.connect("points.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    category TEXT NOT NULL
)
""")

# PONTOS DE TESTE
cursor.execute("DELETE FROM points")

points = [
    ("Ponto Teste 1", "Rua A, Porto Alegre", -30.03, -51.20, "eletronico"),
    ("Ponto Teste 2", "Rua B, Porto Alegre", -30.05, -51.22, "eletronico")
]

cursor.executemany(
    "INSERT INTO points (name, address, lat, lng, category) VALUES (?, ?, ?, ?, ?)", 
    points
)

conn.commit()
conn.close()

print("Seed concluído.")
