# Classe que representa o relacionamento entre livro e genero
from dataclasses import dataclass

@dataclass
class LivroGenero:
    livroCodigo: int = None
    generoCodigo: int = None