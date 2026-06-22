# Classe que representa o relacionamento entre livro e genero
from dataclasses import dataclass

@dataclass
class LivroGenero:
    livro_id: int = None
    genero_id: int = None