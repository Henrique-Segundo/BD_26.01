# Classe que representa a entidade pessoa
from dataclasses import dataclass

@dataclass
class Pessoa:
    codigo: int = None
    nome: str = ""
    login: str = ""
    senha: str = ""