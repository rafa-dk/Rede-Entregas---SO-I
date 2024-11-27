from collections import deque
import time
import random
import threading


class Caminhao(threading.Thread):
    
    def __init__(self, id, carga_maxima, dist_proximo_posto):
        super().__init__()  # Chama o construtor da classe base threading.Thread
        self.id = id
        self.carga_maxima = carga_maxima
        self.distancia_proximo_posto = dist_proximo_posto # *** não usamos ainda, retirar se for o caso!
        self.posto_atual = None
        self.fila_encomendas = deque()
        self.semaforo = threading.Semaphore(carga_maxima)  # Semáforo para controlar os espaços de carga
        pass

        def run(self):
            while True:
                # Lógica do loop do caminhão
                pass

    def getCargasLivres(self):
        return self.carga_maxima - len(self.fila_encomendas)


    def irProProximoPosto (self, primeiro_posto): # Usar na main durante a primeira viagem do caminhão
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual = primeiro_posto  
        
        for encomenda in self.fila_encomendas:
            if encomenda.dest == self.posto_atual.getPostoNum():
                self.deixarEncomenda()
            elif primeiro_posto.getFilaDespachoQuantidade() > 0:
                self.pegarEncomenda()
            else:
                self.irProProximoPosto(self.posto_atual.getProximoPosto())
        pass

    
    def irProProximoPosto (self, proximo_posto):
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual = proximo_posto # Consertar : Quando estiver saindo do último posto, não aumentar 1, mas sim, voltar ao posto 1.
        
        for encomenda in self.fila_encomendas:
            if encomenda.dest == self.posto_atual.getPostoNum():
                self.deixarEncomenda()
            elif self.posto_atual.getFilaDespachoQuantidade() > 0 and self.semaforo._value > 0: # Entra na fila caso possua espaços livres 
                self.pegarEncomenda()
            else:
                self.irProProximoPosto(self.posto_atual.getProximoPosto()) # Vai pro próximo posto direto
        pass

    def pegarEncomenda (self):
        
        while (self.posto_atual.getFilaDesapachoQuantidade() > 0 and self.semaforo._value > 0):
            with self.posto_atual.lock:  # Garante exclusividade ao operar no ponto
                encomenda = self.posto_atual.enviarEncomenda()
                self.fila_encomendas.append(encomenda)
                self.semaforo.acquire()  # Reserva um espaço
                encomenda.setCarregado(time.time())  # Atualiza o log
                time.sleep(random.uniform(0.1, 0.5)) # Tempo de despacho

        self.irProProximoPosto(self.posto_atual.getProxPosto())
        pass

    def deixarEncomenda (self):
        with self.posto_atual.lock:  # Garante exclusividade ao operar no ponto
            for encomenda in list(self.fila_encomendas):
                if (encomenda.dest == self.posto_atual.getPostoNum()):
                    self.fila_encomendas.remove(encomenda)
                    self.semaforo.release()  # Libera um espaço
                    encomenda.setDescarregado(time.time())  # Atualiza o log
                    self.posto_atual.receberEncomenda(encomenda)
                    time.sleep(random.uniform(0.1, 0.5)) # Tempo de despacho

        self.pegarEncomenda()
        pass