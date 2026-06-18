# Classe que representa o relacionamento entre livro e usuario
from dataclasses import dataclass

@dataclass
class Diario:
    LivroCodigo: int = None
    UsuarioCodigo: int = None
    nota: str = ""
    review: str = ""
    dataVisualizacao: str = ""