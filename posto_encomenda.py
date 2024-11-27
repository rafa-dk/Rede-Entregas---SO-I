from collections import deque
import time
import random
import threading

class postoEncomenda:
 

    def __init__(self, num):
        self.num = num
        self.proximo_posto = None # Duranante a criação dos postos, na próxima iteração, setar o próximo posto do posto anterior.
        self.fila_caminhoes = deque()
        self.fila_encomendas = deque()
        self.fila_despacho = deque()
        self.lock = threading.Lock()  # Mutex para controlar um veículo por vez
        pass

    def run(self, qtd_postos):
        if (self.num != qtd_postos):
            self.setProxPosto(self.num + 1)
        else:
            self.setProxPosto(0)
        pass

    def setProxPosto (self, proximo_posto):
        self.proximo_posto = proximo_posto
        pass
    
    def getProxPosto (self):  
        return self.proximo_posto 

    def getPostoNum (self):
        return self.num
    
    def getFilaDespachoQuantidade(self):
        return len(self.fila_despacho)

    
    def enviarEncomenda (self):
        if self.fila_despacho:
            encomenda = self.fila_despacho[0]
            encomenda_aux = encomenda
            self.fila_despacho.remove(encomenda)
            return encomenda_aux
        return -1
 
    def receberEncomenda (self, encomenda):
        self.fila_encomendas.append(encomenda) 
        pass

    def chegarEncomenda (self, encomenda): # Quando a encomenda é inicializada, ela chega num ponto de encomenda
        self.fila_despacho.append(encomenda) 
        pass

    def liberarCaminhao (self):
        self.fila_caminhoes[0].irProProximoPosto()
        self.fila_caminhoes.popleft()
        pass
    