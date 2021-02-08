NORTE='Norte'   #VARIÁVEL CONSTANTE
SUL= 'Sul'
LESTE= 'Leste'
OESTE= 'Oeste'



class Motor:  # definindo a classe motor
    def __init__(self):  # criação do atributo velocidade
        self.velocidade = 0

    def acelerar(self):  #Criação do método acelerar
        self.velocidade += 1

    def frear(self):     #Criação do método frear
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade) # função que controla a velocidade mínima possível 0


class Direcao: #Criação da classe direção
 rotação_a_direita_dct = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE} #dictionari
 rotação_a_esquerda_dct ={NORTE:OESTE,LESTE:NORTE,SUL:LESTE,OESTE:SUL}
    def __init__(self): #criação do atributo valor_de_direcao
        self.Valor = NORTE #valor inicial começa na direção norte
    def girar_a_direita(self):
        self.Valor=self.rotação_a_direita_dct[self.Valor]
    def girar_a_esquerda(self):
        self.valor=self.rotação_a_esquerda_dct[self.Valor]






