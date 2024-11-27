import threading
import time
import random

class Encomenda(threading.Thread):

    def __init__(self, id, qtd_posto_enc, pontos):
        super().__init__()  # Chama o construtor da classe base threading.Thread
        self.pontos = pontos
        self.id = id
        self.orig = random.randint(0, qtd_posto_enc-1)
        self.dest = self.orig
        while self.dest == self.orig:
            self.dest = random.randint(0, qtd_posto_enc-1)
        self.horario_chegada = None
        self.horario_carregado = 0
        self.caminhao = None
        self.horario_descarregado = None

    def run(self):
        print(f"Encomenda {self.id} iniciando...")
        for i in range(len(self.pontos)):
            if self.orig == self.pontos[i].getPostoNum():
                self.pontos[i].chegarEncomenda(self)
                self.horario_chegada = time.time()
                print(f"Encomenda {self.id} chegou, com origem no posto {self.orig} para o posto {self.dest}")
                break 
        while self.horario_descarregado is None:
            time.sleep(1)
            print(f"Encomenda {self.id} chegou ao destino (posto {self.dest})")
        self.escreverArq() 
        pass
        
    def setChegada(self, horario):
        self.horario_chegada = horario

    def setCarregado(self, horario):
        self.horario_carregado = horario

    def setCaminhao(self, caminhao):
        self.caminhao = caminhao

    def setDescarregado(self, horario):
        self.horario_descarregado = horario

    def getId(self):
        return self.id
    
    def getOrig(self):
        return self.orig
    
    def getRest(self):
        return self.dest


    def escreverArq(self):
        filename = f"encomenda_{self.id}_log.txt"
        with open(filename, "w") as file:
            file.write(f"Numero da Encomenda: {self.id}\n")
            file.write(f"Ponto de Origem: {self.orig}\n")
            file.write(f"Ponto de Destino: {self.dest}\n")
            file.write(f"Horario de Chegada ao Ponto de Origem: {self.horario_chegada}\n")
            file.write(f"Horario de Carregamento no Veiculo: {self.horario_carregado}\n")
            file.write(f"Identificador do Caminhao: {self.caminhao.getID()}\n")
            file.write(f"Horario de Descarregamento: {self.horario_descarregado}\n")