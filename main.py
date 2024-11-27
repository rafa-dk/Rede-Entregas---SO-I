import threading
from collections import deque
import time
import random
from caminhao import Caminhao
from encomenda import Encomenda
from posto_encomenda import postoEncomenda

def receberParametros ():
    flag = False
    while flag == False: # Verficacao de segurança dos parâmetros
        n_pontos_distribuicao = int(input("Digite o numero de pontos de distribuicao: "))
        n_caminhoes = int(input("Digite o numero de caminhoes: "))
        n_encomendas = int(input("Digite o numero de encomendas totais: "))
        n_carga_maxima_caminhoes = int(input("Digite o numero de encomendas que cada caminhao pode carregar: "))
        if n_encomendas > n_carga_maxima_caminhoes and n_carga_maxima_caminhoes > n_caminhoes:
            flag = True 
        else:
            print("A seguinte regra deve ser seguida! : n_encomendas >> n_carga_maxima_caminhoes >> n_caminhoes")

    return n_pontos_distribuicao, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes

def getPosto(posto):
    return postos[posto]

 

def inicializar_pontos(n_pontos, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes):
    # Criando pontos de redistribuição
    pontos = [postoEncomenda(i) for i in range(n_pontos)]
    for i in range(n_pontos):
        pontos[i].setProxPosto(pontos[(i + 1) % n_pontos])
    return pontos

def liberar_threads(threads):
    for thread in threads:
        print(f"{thread.name} liberado")
        thread.join()
    print("\nO programa acabou")

if __name__ == "__main__":

    n_pontos, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes = receberParametros()
    pontos = inicializar_pontos(n_pontos, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes)

    threads_encomendas = []
    threads_caminhoes = []
 

    parada = 0

    postos = []
    for i in range(n_pontos):
        postos.append(i)

    for i in range(n_encomendas):
        thread = Encomenda(i, n_pontos, pontos)
        thread.name = f"Encomenda {i}"  # Atualizado para evitar o DeprecationWarning
        threads_encomendas.append(thread)
        thread.start()

    for i in range(n_caminhoes):
        thread = Caminhao(i, n_carga_maxima_caminhoes, pontos, parada)
        thread.name = f"Caminhao {i}"
        threads_caminhoes.append(thread)
        thread.start()
    #

     
    liberar_threads(threads_encomendas + threads_caminhoes)

 