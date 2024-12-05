from dataclasses import dataclass

from projeto.Funcionario import Funcionario


@dataclass
class Motorista(Funcionario):
    cnh:str

    def mostrar_dados_funcionarios(self):
        return "Mostrando dados Motorista"