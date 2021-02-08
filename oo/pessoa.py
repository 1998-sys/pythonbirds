class Pessoa: #As classes devem começar com letra maiúscula
    olhos = 2 #Atributo de classe (mesmo valor para todos os atributos), economia de alocação de memória
    def __init__(self, *filhos,nome = None,idade=35): #Atributo
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self): #método está sempre atrelado auma classe
        return f'olá {id(self)}'
    @staticmethod
    def metodo_estatico():
        return 42
    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem (Pessoa):
    pass

if __name__ == '__main__':
    renzo = Homem(nome='Renzo')
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
    print(Joao.__dict__) #mostra todos os atributos de instância de um objeto
    print(renzo.__dict__) #mostra todos os atrubutos
    print(Pessoa.olhos) #Acessando o valor do atributo da classe globalmente
    print(Joao.olhos) #Acessando o atributo olhos através do objeto (João)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(renzo.olhos), id(Joao.olhos)) #mesmo ID para todos
    print(Pessoa.metodo_estatico(),Joao.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), Joao.nome_e_atributos_de_classe())