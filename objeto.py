class Pessoa:
    nome: str
    idade: int
    peso: float

variavel = Pessoa()

variavel.nome = input("Digite seu nome:")
variavel.idade = int(input("Digite sua idade:"))
variavel.peso = float(input("Digite seu peso:"))