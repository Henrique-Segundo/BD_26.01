import datetime
# Classe que representa a entidade pessoa
from dataclasses import dataclass

@dataclass
class Livros:
    id: int = None
    nome: str = ""
    descricao: str = ""
    data_de_publicacao: datetime = ""