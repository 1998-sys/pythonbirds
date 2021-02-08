class Pessoa: #As classes devem começar com letra maiúscula
    def __init__(self, *filhos,nome = None,idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self): #método está sempre atrelado auma classe
        return f'olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    Joao = Pessoa(renzo,nome ='João')
    print(Pessoa.cumprimentar(Joao))
    print(id(Joao))
    print(Joao.cumprimentar())
    print(Joao.nome)
    print(Joao.idade)
    for filho in Joao.filhos:
        print(filho.nome)