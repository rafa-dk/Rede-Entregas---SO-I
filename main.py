import threading
import time
import random

def receberParametros (n_pontos_distribuicao, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes):
    n_pontos_distribuicao = input("Digite o numero de pontos de distribuicao: ")
    n_caminhoes = input("Digite o numero de caminhoes ")
    n_encomendas = input("Digite o numero de encomendas totais: ")
    n_carga_maxima_caminhoes = input("Digite o numero de encomendas que cada caminhao pode carregar: ")
    return n_pontos_distribuicao, n_caminhoes, n_encomendas, n_carga_maxima_caminhoes


