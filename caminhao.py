from collections import deque
import time
import random
import threading
from encomenda import Encomenda


class Caminhao(threading.Thread):
    
    def __init__(self, id, carga_maxima, pontos, parada):
        super().__init__()  # Chama o construtor da classe base threading.Thread
        self.id = id 
        self.parada = parada
        self.carga_maxima = carga_maxima
        self.posto_atual = random.choice(pontos)
        self.fila_encomendas = deque()
        self.semaforo = threading.Semaphore(carga_maxima)  # Semáforo para controlar os espaços de carga
        pass

    def run(self): 
        self.irProProximoPosto(self.posto_atual.getProxPosto())
        pass

    def getCargasLivres(self):
        return self.carga_maxima - len(self.fila_encomendas)

    def getID(self):
        return self.id
 
    def irProProximoPosto(self, proximo_posto):
        if self.parada == 1:
            return
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual = proximo_posto  # Define o próximo posto como uma instância de postoEncomenda
 
        for encomenda in self.fila_encomendas:
            if encomenda.dest == self.posto_atual.getPostoNum():
                self.deixarEncomenda()
        if self.posto_atual.getFilaDespachoQuantidade() > 0 and self.semaforo._value > 0:
            self.pegarEncomenda()
        else:
            self.irProProximoPosto(self.posto_atual.getProxPosto())

    def pegarEncomenda (self):
        
        while (self.posto_atual.getFilaDespachoQuantidade() > 0 and self.semaforo._value > 0):
            with self.posto_atual.lock:  # Garante exclusividade ao operar no ponto
                
                encomenda = self.posto_atual.enviarEncomenda()
                self.fila_encomendas.append(encomenda)
                self.semaforo.acquire()  # Reserva um espaço
                encomenda.setCarregado(time.time())  # Atualiza o log
                encomenda.setCaminhao(self)
                time.sleep(random.uniform(0.1, 0.5)) # Tempo de despacho
                print(f"Caminhao {self.id} pegou a encomenda {encomenda.id} no posto {self.posto_atual.getPostoNum()}")

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
                    print(f"Caminhao {self.id} deixou a encomenda {encomenda.id} no posto {self.posto_atual.getPostoNum()}")

        self.pegarEncomenda()
        pass
