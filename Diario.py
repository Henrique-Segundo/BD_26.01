# Classe que representa o relacionamento entre livro e usuario
from dataclasses import dataclass

@dataclass
class Livro:
    LivroCodigo: int = None
    UsuarioCodigo: int = None
    nota: str = ""
    review: str = ""
    dataVisualizacao: str = ""