# pip3 install mariadb

import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="Hola1234",
        host="127.0.0.1",
        port=3306,
        database="tienda"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("SELECT nombre, precio FROM producto")

print(f"{'  Nombre':40} {'  Precio':10}")
print(f"---------------------------------------- ----------")

for (nombre, precio) in cur:
    print(f"{nombre:40} {precio:10}")

cur.execute(
    "INSERT INTO producto (codigo, nombre, precio, codigo_fabricante) VALUES (?, ?, ?, ?)",
    (13, 'AMD RX 6700XT', 459, 7))

cur.execute(
    "SELECT nombre, precio FROM producto WHERE nombre=?",
    ('AMD RX 6700XT',)
)

print()
for (nombre, precio) in cur:
    print(f"Nombre: {nombre}, Precio: {precio}")
