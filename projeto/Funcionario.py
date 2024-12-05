from abc import ABC, abstractmethod
from dataclasses import dataclass

from projeto.Endereco import Endereco

@dataclass
class Funcionario(ABC):
    nome:str
    idade:int
    endereco:Endereco
    
    @abstractmethod
    def mostrar_dados_funcionarios(self):
        pass

