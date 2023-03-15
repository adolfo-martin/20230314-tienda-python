from dataclasses import dataclass

@dataclass
class Config:
    user: str = "adolfo",
    password: str = "Hola1234",
    host: str = "10.0.0.2",
    port: str = 3306,
    database: str = "tienda"
