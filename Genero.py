# Classe que representa a entidade genero
from dataclasses import dataclass

@dataclass
class Genero:
    codigo: int = None
    nome: str = ""
    descricao: str = ""