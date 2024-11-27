import threading
import time
import random

class Encomenda:

    def __init__(self, id, qtd_posto_enc):
        self.id = id
        self.orig = random.randint(0, qtd_posto_enc-1)
        self.dest = self.orig
        while self.dest == self.orig:
            self.dest = random.randint(0, qtd_posto_enc-1)
        self.horario_chegada = None
        self.horario_carregado = None
        self.caminhao = None
        self.horario_descarregado = None
        
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

    #Nao precisa necessariamente ser um metodo dessa classe
    def monitoramento(qtd_posto_enc, lista_encomenda, caminhao):
        print("\n--- Monitoramento em tempo real ---")
        for i in range(qtd_posto_enc):
            #lista_encomenda = [[] for _ in range(S)]  ==> Filas nos pontos de redistribuição
            print(f"Ponto {i}: {len(lista_encomenda[i])} encomendas aguardando.")
        for i, caminhao in enumerate(caminhao):
            print(f"Veículo {i}: No ponto {caminhao.get('point', 'N/A')} com {caminhao.get('load', 0)} encomendas.")
        print("------------------------------------")
        time.sleep(1)

    def escreverArq(self):
        filename = f"encomenda_{self.id}_log.txt"
        with open(filename, "w") as file:
            file.write(f"Numero da Encomenda: {self.id}\n")
            file.write(f"Ponto de Origem: {self.orig}\n")
            file.write(f"Ponto de Destino: {self.dest}\n")
            file.write(f"Horario de Chegada ao Ponto de Origem: {self.horario_chegada}\n")
            file.write(f"Horario de Carregamento no Veiculo: {self.horario_carregado}\n")
            file.write(f"Identificador do Caminhao: {self.caminhao}\n")
            file.write(f"Horario de Descarregamento: {self.horario_descarregado}\n")