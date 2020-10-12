class Carro :
    def __init__(self,modeloCarro,marcaCarro,numeroPortas):
        self.modeloCarro = modeloCarro
        self.marcaCarro = marcaCarro
        self.numeroPortas = numeroPortas
        print("Carro cadastrado com sucesso")
    def get_modeloCarro(self):
        return self.modeloCarro
    def set_modeloCarro(self, novo_modeloCarro):
     self.modeloCarro = novo_modeloCarro


carro_1 = Carro("Fiat","UnoMille", 4)
carro_1.set_modeloCarro("Strava")
print("Modelo do carro foi atualizado: ", carro_1.get_modeloCarro())