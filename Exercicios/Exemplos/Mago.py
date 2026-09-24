class Mago:
    pontos_de_vida: int
    pontos_de_magia: int
    capcidade: int = 50

    def __init__(self, pontos_de_vida:int, pontos_de_magia:int):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_magia = pontos_de_magia

#instância

mago = Mago(30, 50)        