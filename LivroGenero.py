# Classe que representa o relacionamento entre livro e genero
from dataclasses import dataclass

@dataclass
class Usuario:
    livroCodigo: int = None
    GeneroCodigo: int = None