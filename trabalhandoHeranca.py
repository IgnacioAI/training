# esses codigos devem ser rodados em notebook

class Formas:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    definicao = "A forma ainda não foi definida"
    autor = "Ainda não foi definido um autor para ela"
    def area(self):
        return self.x * self.y
    def get_perimetro(self):
        return 2 * self.x +2 * self.y
    def set_descricao(self,texto):
        self.descricao = texto
    def set_nome_do_autor(self,texto):
        self.autor = texto
    def self_escala(self,escala):
        self.x = self.x * escala
        self.y = self.y * escala
        
retangulo = Formas(5,8)


retangulo.area()

quadrado = Formas(7,7)


class Quadrado(Formas):
    def __init__(self,x):
        self.x = x
        self.y = x
 
 
 #acessando os metodos da classe pai
 
class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
    def area(self):
        return self.comprimento * self.largura
    def perimetro(self):
        return 2 * self.comprimento + 2 * self.largura
    
# quadrado como um aheranç a do retangulo
class Quadrado:
    def __init__(self,comprimento):
        super().__init__(comprimento,comprimento) 
        
#instanciando o objeto quadrado
quadrado=Quadrado(6)
print(quadrado.perimetro())