import time
import random

class Veiculo:
    
    def __init__(self, carga_maxima, dist_proximo_posto):
        self.carga_maxima = carga_maxima
        self.distancia_proximo_posto = dist_proximo_posto
        self.posto_atual = 0
        pass

    def irProProximoPosto (self):
        time.sleep(random.uniform(0.1, 0.5))
        self.posto_atual += 1 # Consertar : Quando estiver saindo do último posto, não aumentar 1, mas sim, voltar ao posto 1.
        pass

    def pegarPacote (self):

        pass