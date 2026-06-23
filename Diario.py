import datetime
# Classe que representa o relacionamento entre livro e usuario
from dataclasses import dataclass

@dataclass
class Diario:
    livro_id: int = None
    usuario_id: int = None
    nota: str = ""
    review: str = ""
    data: datetime = ""