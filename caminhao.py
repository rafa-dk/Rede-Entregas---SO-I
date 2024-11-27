from collections import deque
import time
import random


class Caminhao:
    
    def __init__(self, id, carga_maxima, dist_proximo_posto):
        self.id = id
        self.carga_maxima = carga_maxima
        self.distancia_proximo_posto = dist_proximo_posto # *** não usamos ainda, retirar se for o caso!
        self.posto_atual = None
        self.fila_encomendas = deque()
        pass

    def getCargasLivres(self):
        return self.carga_maxima - len(self.fila_encomendas)


    def irProProximoPosto (self, primeiro_posto): # Usar na main durante a primeira viagem do caminhão
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual = primeiro_posto  
        
        for encomenda in self.fila_encomendas:
            if encomenda.dest == self.posto_atual.getPostoNum():
                primeiro_posto.receberCaminhao(self)
            elif primeiro_posto.getFilaDespachoQuantidade() > 0:
                primeiro_posto.receberCaminhao(self)
        pass

    
    def irProProximoPosto (self, proximo_posto):
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual = proximo_posto # Consertar : Quando estiver saindo do último posto, não aumentar 1, mas sim, voltar ao posto 1.
        
        for encomenda in self.fila_encomendas:
            if encomenda.dest == self.posto_atual.getPostoNum():
                self.posto_atual.receberCaminhao(self)
            elif self.posto_atual.getFilaDespachoQuantidade() > 0 and self.getCargasLivres() > 0: # Entra na fila caso possua espaços livres 
                self.posto_atual.receberCaminhao(self)
            else:
                self.irProProximoPosto(self.posto_atual.getProximoPosto()) # Vai pro próximo posto direto
        pass

    def pegarEncomenda (self, encomenda):
        self.fila_encomendas.append(encomenda)
        #encomenda.setCarregado() # Atualizar o log da encomenda
        pass

    def deixarEncomenda (self, encomenda):
        # pop da encomenda, mas precisa ser aquela encomenda específica!
        self.fila_encomendas.remove(encomenda)
        #encomenda.setDescarregado()
        pass