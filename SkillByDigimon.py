# Classe que representa a entidade Skill by Digimon (Habilidades por digimon)
from dataclasses import dataclass


# Apresenta erros conceituais que devem ser corridigos no bando de dados
#1 number e digimon são a mesma informação
#2 skill está como string mas poderia ser um inteiro chave estrangeira de skill

@dataclass
class SkillByDigimon:
    codigo: int = None
    number: int = ""
    digimon: str = ""
    skill: str = ""
    level: int = ""