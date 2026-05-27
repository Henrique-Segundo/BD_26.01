# Classe que representa a entidade Digivolution Requirements (Requisitos de Digievolução)
from dataclasses import dataclass

# Apresenta erros conceituais que devem ser corridigos no bando de dados
#1 number e digimon são a mesma informação

@dataclass
class DigivolutionRequirements:
    number: int = ""
    digimon: str = ""
    level: int = ""
    hp: int = ""
    sp: int = ""
    atk: int = ""
    defesa: int = ""
    spd: int = ""
    abi: int = ""
    cam: int = ""
    extraCondition: str = ""