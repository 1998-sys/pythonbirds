class Pessoa: #As classes devem começar com letra maiúscula
    def __init__(self, nome = None,idade=35):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self): #método está sempre atrelado auma classe
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('João')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Matheus'
    print(p.nome)
    print(p.idade)