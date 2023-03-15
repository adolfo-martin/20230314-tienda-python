from dataclasses import dataclass

@dataclass
class Config:
    user: str = "adolfo"
    password: str = "Hola1234"
    host: str = "127.0.0.1"
    port: str = 3306
    database: str = "tienda"
