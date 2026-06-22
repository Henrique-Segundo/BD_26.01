# Classe que representa a entidade genero
from dataclasses import dataclass

@dataclass
class Genero:
    id: int = None
    nome: str = ""
    descricao: str = ""