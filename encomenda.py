import threading
import time
import random

class Encomenda:
    def __init__(self, num, org, dest):
        self.num = num
        self.org = org
        self.dest = dest
        self.horario_chegada = None
        self.horario_carregado = None
        self.num_caminhao = None
        self.horario_descarregado = None

    def monitoramento(self):
        print(f'{self.num=}')
        print(f'{self.org=}')
        print(f'{self.dest=}')
        print(f'{self.horario_chegada=}')
        print(f'{self.num_caminhao=}')
        print(f'{self.horario_descarregado=}')

    def escrever_arq(self):

        filename = f"package_{self.num}_log.txt"
        with open(filename, "w") as file:
            file.write("Número da Encomenda: {}\n".format(self.num))
            file.write("Ponto de Origem: {}\n".format(log["origin"]))
            file.write("Ponto de Destino: {}\n".format(log["destination"]))
            file.write("Horário de Chegada ao Ponto de Origem: {}\n".format(log["arrival_time"]))
            file.write("Horário de Carregamento no Veículo: {}\n".format(log["load_time"]))
            file.write("Identificador do Veículo: {}\n".format(log["vehicle_id"]))
            file.write("Horário de Descarregamento: {}\n".format(log["unload_time"]))