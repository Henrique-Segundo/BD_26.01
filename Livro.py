# Classe que representa a entidade pessoa
from dataclasses import dataclass

@dataclass
class Livro:
    codigo: int = None
    nome: str = ""
    descricao: str = ""
    dataPublicacao: str = ""