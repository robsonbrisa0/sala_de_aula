class Carta:
    conteudo: str
    destinatario: str
    remetente: str
    
    def __init__(self, conteudo:str, destinatario:str, remetente:str):
        self.conteudo = conteudo
        self.destinatario = destinatario
        self.remetente = remetente
       

#instância

carta = Carta("Bom dia", "Robson", "Bob") 