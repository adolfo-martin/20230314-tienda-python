# pip3 install mysql-connector-python

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

import mysql.connector
import sys

try:
    conn = mysql.connector.connect(
        user = "adolfo",
        password = "Hola1234",
        host = "10.0.0.2",
        port = 3306,
        database = "tienda"
    )
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

cur.execute("SELECT nombre, precio FROM producto")

print(f"{'  Nombre':40} {'  Precio':10}")
print(f"---------------------------------------- ----------")

for (nombre, precio) in cur:
    print(f"{nombre:40} {precio:10}")
