class Pessoa: #As classes devem começar com letra maiúscula
    def cumprimentar(self): #método está sempre atrelado auma classe
        return f'olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())