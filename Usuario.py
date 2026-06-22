import datetime

# Classe que representa a entidade usuario
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int = None
    nome: str = ""
    descricao: str = ""
    data_de_nascimento: datetime = ""