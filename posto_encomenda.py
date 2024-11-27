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

    def receberCaminhao (self, caminhao):
        self.fila_caminhoes.append(caminhao)
        pass
    
    def enviarEncomenda (self):
        if (len(self.fila_despacho) > 0):
            while (self.fila_caminhoes[0].getCargasLivres() > 0):
                time.sleep(random.uniform(0.1, 0.5)) # Tempo de despacho
                self.fila_caminhoes[0].pegarEncomenda(self.fila_despacho[0])
                self.fila_despacho.popleft()
        self.liberarCaminhao()
        pass
 
    def receberEncomenda (self):
        for encomenda in self.fila_caminhoes[0].fila_encomendas:
            if encomenda.dest == self.num:
                time.sleep(random.uniform(0.1, 0.5)) # Tempo de despacho
                self.fila_encomendas.append(encomenda)
                self.fila_caminhoes[0].deixarEncomenda(self.fila_despacho[0])
                # Encomenda.setCarregado
        self.enviarEncomenda()
        pass

    def liberarCaminhao (self):
        self.fila_caminhoes[0].irProProximoPosto()
        self.fila_caminhoes.popleft()
        pass
    