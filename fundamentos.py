# Herança
# Polimorfismo
# Objetivo:
# Reaproveitar codigos.

from abc import ABC, abstractmethod


class Pessoa(ABC):
    nome:str
    idade:int
    @abstractmethod
    def devers (self):
        pass
    

class Aluno(Pessoa):
    ra:str
    def devers(self):
        return "Estudar"

class Professor(Pessoa):
    matricula:str
    def devers(self):
        return "Ensinar"

aluno = Aluno
professor = Professor

aluno.nome = input("Digite seu nome: ")
aluno.ra = input("Digite seu RA: ")
professor.nome = input("Digite seu nome:")
professor.matricula = input("Digite sua matricula:")