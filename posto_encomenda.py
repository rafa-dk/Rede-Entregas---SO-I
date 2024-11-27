from collections import deque

class postoEncomenda:

    def __init__(self):
        self.fila_caminhoes = deque()
        self.fila_encomendas = deque()
        self.fila_despacho = deque()
        
        pass

    def receberCaminhao (self, caminhao):
        self.fila_caminhoes.append(caminhao)
        pass
    
    def enviarEncomenda (self, encomenda):
        pass


    def receberEncomenda (self, encomenda):
        self.fila_encomendas.append(encomenda)

    def liberarCaminhao (self):
        self.fila_caminhoes.popleft()
        pass
    