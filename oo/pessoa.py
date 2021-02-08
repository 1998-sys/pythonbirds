class Pessoa: #As classes devem começar com letra maiúscula
    def __init__(self, *filhos,nome = None,idade=35): #Atributo
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
    Joao.sobrenome='Ramalho' #Adicionar atributos (atributo dinâmico)
    print(Joao.sobrenome)
    del Joao.filhos #Remover atributos
    print(Joao.__dict__) #mostra todos os atributos
    print(renzo.__dict__) #mostra todos os atrubutos