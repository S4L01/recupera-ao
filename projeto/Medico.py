from dataclasses import dataclass

from projeto import Endereco
from projeto.Funcionario import Funcionario


@dataclass
class Medico(Funcionario):
    crm:str

    def mostrar_dados_funcionarios(self):
        return "Mostrando os dados Medico"