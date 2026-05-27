# Classe que representa a entidade Skill (Habilidades)
from dataclasses import dataclass

@dataclass
class Skill:
    codigo: int = None
    skill: str = ""
    spCost: int = ""
    type: str = ""
    power: int = ""
    attribute: str = ""
    inheritable: bool = ""
    description: str = ""