from collections import deque
import time
import random


class postoEncomenda:
 

    def __init__(self, num):
        self.num = num
        self.proximo_posto = None # Duranante a criação dos postos, na próxima iteração, setar o próximo posto do posto anterior.
        self.fila_caminhoes = deque()
        self.fila_encomendas = deque()
        self.fila_despacho = deque()
        pass

    def setProxPosto (self, proximo_posto):
        self.proximo_posto = proximo_posto
        pass
    
    def getProxPosto (self): # Tratar para caso NONE
        return self.proximo_posto 

    def getPostoNum (self):
        return self.num
    
    def getFilaDesapachoQuantidade(self):
        return len(self.fila_despacho)

    
    def enviarEncomenda (self):
        encomenda = self.fila_despacho[0]
        self.fila_despacho.popleft()
        return encomenda 
 
    def receberEncomenda (self, encomenda):
        self.fila_encomendas.append(encomenda)
        # Encomenda.setCarregado # Atualizar o log da encomenda
        pass

    def liberarCaminhao (self):
        self.fila_caminhoes[0].irProProximoPosto()
        self.fila_caminhoes.popleft()
        pass
    