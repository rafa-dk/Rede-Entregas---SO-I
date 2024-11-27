from collections import deque
import time
import random


class Caminhao:
    
    def __init__(self, carga_maxima, dist_proximo_posto):
        self.carga_maxima = carga_maxima
        self.distancia_proximo_posto = dist_proximo_posto
        self.posto_atual = None
        self.fila_encomendas = deque()
        pass
    
    def irProProximoPosto (self, primeiro_posto): # Usar na main durante a primeira viagem do caminhão
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual = primeiro_posto  
        
        for encomenda in self.fila_encomendas:
            if encomenda.dest == self.posto_atual.getPostoNum():
                primeiro_posto.receberCaminhao(self)
            elif primeiro_posto.getFilaDespachoQuantidade() > 0:
                primeiro_posto.receberCaminhao(self)
        pass

    
    def irProProximoPosto (self):
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual = self.posto_atual.getProximoPosto() # Consertar : Quando estiver saindo do último posto, não aumentar 1, mas sim, voltar ao posto 1.
        
        for encomenda in self.fila_encomendas:
            if encomenda.dest == self.posto_atual.getPostoNum():
                self.posto_atual.receberCaminhao(self)
            elif self.posto_atual.getFilaDespachoQuantidade() > 0:
                self.posto_atual.receberCaminhao(self)
        
        pass

    def pegarPacote (self):

        pass