# Classe que representa a entidade Digivolutions (Digievolução - processo que um digimon se torna outro)
from dataclasses import dataclass

# Apresenta erros conceituais que devem ser corridigos no bando de dados
#1 number e digivolves from são a mesma informação
#2 digivolves to, em vez de string deveria ser uma chave estrangerira para o numero do digimon que evolui

@dataclass
class Digivolution:
    codigo: int = None
    number: int = ""
    digivolvesFrom: str = ""
    digivolvesTo: str = ""