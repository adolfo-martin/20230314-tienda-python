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
        connection = mysql.connector.connect(
            user = self.config.user,
            password = self.config.password,
            host = self.config.host,
            port = self.config.port,
            database = self.config.database,
        )
        return connection

    def retrieve_products(self) -> list[Product]: 
        try:
            connection = self.__create_connection()
        except mysql.connector.Error as error:
            message = f"Error connecting to database {self.config.database}: {error}"
            raise StoreRepositoryError(message)

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT codig, nombre, precio FROM producto")

            products: list[Product] = []
            for (codigo, nombre, precio) in cursor:
                products.append(Product(codigo, nombre, precio))

            cursor.close()
            return products
        except Exception as error:
            message = f"Error connecting to database {self.config.database}"
            raise StoreRepositoryError(message)
        finally:
            connection.close()


@dataclass 
class StoreRepositoryError(Exception):
    pass
