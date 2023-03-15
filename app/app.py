import sys
import subprocess
from StoreRepository import StoreRepository, StoreRepositoryError
from Config import Config
from Product import Product

def main():
    # clear_screen()

    config = Config()
    repository = StoreRepository(config)
    try:
        products: list[Product] = repository.retrieve_products()
    except StoreRepositoryError as error:
        print(f"Error retrieving products: {error}")
        sys.exit(1)

    render_products(products)

def clear_screen():
    subprocess.run(['clear'])


def render_products(products: list[Product]) -> None:
    print(f"{'  Nombre':40} {'  Precio':10}")
    print(f"---------------------------------------- ----------")

    for product in products:
        print(f"{product.name:40} {product.price:10}")


if __name__ == '__main__':
    main()