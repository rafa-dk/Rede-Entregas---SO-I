import threading
import time
import random

class Encomenda:
    def __init__(self, num, orig, dest):
        self.num = num
        self.orig = orig
        self.dest = dest
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
        return self.num

    def monitoramento(self):
        print(f'{self.num=}')
        print(f'{self.orig=}')
        print(f'{self.dest=}')
        print(f'{self.horario_chegada=}')
        print(f'{self.horario_carregado=}')
        print(f'{self.caminhao=}')
        print(f'{self.horario_descarregado=}')

    def escreverArq(self, log):
        filename = f"package_{self.num}_log.txt"
        with open(filename, "w") as file:
            file.write("Numero da Encomenda: {}\n".format(self.num))
            file.write("Ponto de Origem: {}\n".format(log["orig"]))
            file.write("Ponto de Destino: {}\n".format(log["dest"]))
            file.write("Horario de Chegada ao Ponto de Origem: {}\n".format(log["horario_chegada"]))
            file.write("Horario de Carregamento no Veiculo: {}\n".format(log["horario_carregado"]))
            file.write("Identificador do Caminhao: {}\n".format(log["caminhao"]))
            file.write("Horario de Descarregamento: {}\n".format(log["horario_descarregado"]))