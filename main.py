import threading
import time
import random
from caminhao import Caminhao
from encomenda import Encomenda
from posto_encomenda import postoEncomenda

def receberParametros ():
    n_pontos_distribuicao = int(input("Digite o numero de pontos de distribuicao: "))
    n_caminhoes = int(input("Digite o numero de caminhoes: "))
    n_encomendas = int(input("Digite o numero de encomendas totais: "))
    n_carga_maxima_caminhoes = int(input("Digite o numero de encomendas que cada caminhao pode carregar: "))
    return n_pontos_distribuicao, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes


# Configuração do Sistema
def inicializar_sistema(n_pontos, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes):
    # Criando pontos de redistribuição
    pontos = [postoEncomenda(i) for i in range(n_pontos)]
    for i in range(n_pontos):
        pontos[i].setProxPosto(pontos[(i + 1) % n_pontos])

    # Criando caminhões
    caminhoes = [Caminhao(i, n_carga_maxima_caminhoes, n_encomendas) for i in range(n_caminhoes)]
    for i, caminhao in enumerate(caminhoes):
        caminhao.posto_atual = pontos[i % n_pontos]  # Inicia em pontos diferentes

    # Criando encomendas
    encomendas = [Encomenda(i, n_pontos) for i in range(n_encomendas)]
    for encomenda in encomendas:
        pontos[encomenda.orig].fila_despacho.append(encomenda)

    return pontos, caminhoes, encomendas


if __name__ == "__main__":

    n_pontos, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes = receberParametros()
    pontos, caminhoes, encomendas = inicializar_sistema(n_pontos, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes)

    # Iniciando os threads
    for caminhao in caminhoes:
        print(1)
        caminhao.start()

    for encomenda in encomendas:
        print(2)
        encomenda.start()

    # Aguardando a conclusão
    for caminhao in caminhoes:
        print(3)
        caminhao.join()

    for encomenda in encomendas:
        print(4)
        encomenda.join()
