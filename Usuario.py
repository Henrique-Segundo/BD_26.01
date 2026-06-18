# Classe que representa a entidade usuario
from dataclasses import dataclass

@dataclass
class Usuario:
    codigo: int = None
    nome: str = ""
    descricao: str = ""
    dataPublicacao: str = ""