import sys
from StoreRepository import StoreRepository
from Config import Config
from Product import Product
import mysql.connector

config = Config()
repository = StoreRepository(config)
try:
    products: list[Product] = repository.retrieve_products()
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)