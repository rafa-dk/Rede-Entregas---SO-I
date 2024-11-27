import threading
import time
import random

class Encomenda:

    def __init__(self, id, S):
        self.id = id
        self.orig = random.randint(0, S-1)
        self.dest = random.randint(0, S-1)
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

    def getNum(self):
        return self.id
    
    def getOrig(self):
        return self.orig
    
    def getRest(self):
        return self.dest

    #Nao precisa necessariamente ser um metodo dessa classe
    def monitoramento(S, lista_pontos, caminhao):
        print("\n--- Monitoramento em tempo real ---")
        for i in range(S):
            print(f"Ponto {i}: {len(lista_pontos[i])} encomendas aguardando.")
        for i, caminhao in enumerate(caminhao):
            print(f"Veículo {i}: No ponto {caminhao.get('point', 'N/A')} com {caminhao.get('load', 0)} encomendas.")
        print("------------------------------------")
        time.sleep(1)

    def escreverArq(self, log):
        filename = f"package_{self.id}_log.txt"
        with open(filename, "w") as file:
            file.write("Numero da Encomenda: {}\n".format(self.id))
            file.write("Ponto de Origem: {}\n".format(log["orig"]))
            file.write("Ponto de Destino: {}\n".format(log["dest"]))
            file.write("Horario de Chegada ao Ponto de Origem: {}\n".format(log["horario_chegada"]))
            file.write("Horario de Carregamento no Veiculo: {}\n".format(log["horario_carregado"]))
            file.write("Identificador do Caminhao: {}\n".format(log["caminhao"]))
            file.write("Horario de Descarregamento: {}\n".format(log["horario_descarregado"]))