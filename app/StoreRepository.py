from dataclasses import dataclass
import mysql.connector
from Config import Config
from Product import Product


@dataclass
class StoreRepository:
    config: Config

    def __init__(self, config: Config):
        self.config = config

    def __create_connection(self):
            self.connection = mysql.connector.connect(
                user = self.config.user,
                password = self.config.password,
                host = self.config.host,
                port = self.config.port,
                database = self.config.database
            )

    def retrieve_products(self) -> list[Product]: 
        try:
            connection = self.create_connection(self.config)
        except mysql.connector.Error as error:
            message = f"Error connecting to database {self.config.database}: {error}"
            raise StoreRepositoryError(message)

        cursor = connection.cursor()
        cursor.execute("SELECT nombre, precio FROM producto")

        print(f"{'  Nombre':40} {'  Precio':10}")
        print(f"---------------------------------------- ----------")

        for (nombre, precio) in cursor:
            print(f"{nombre:40} {precio:10}")


@dataclass 
class StoreRepositoryError(Exception):
    pass
