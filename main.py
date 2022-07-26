import time
import math

from metodos_construtivos import *
from grasp import *

arq = "data_TSP/att48_d.txt"
#arq = "data_TSP/dantzig42_d.txt"
#arq = "data_TSP/fri26_d.txt"
#arq = "data_TSP/gr17_d.txt"
#arq = "data_TSP/p01_d.txt"
#arq = "data_TSP/five_d.txt"

def ler_arquivo():
    arquivo = open(arq).read()
    matriz = []
    for linha in arquivo.split('\n')[:-1]:
        matriz.append(linha.split())

    matrizNum = []
    for line in matriz:
        matrizNum.append(list(map(float, line)))

    return matrizNum


def inf_para_distancia_zero(matriz):
    for i in range(0, len(matriz)):
        matriz[i][i] = math.inf


if __name__ == '__main__':
    #Carregar dados
    data = ler_arquivo()
    inf_para_distancia_zero(data)
    #print(data)

    #Vizinho mais próximo
    t_inicio = time.time()
    tam_rota, rota, tamanhos_cidades = vizinho_mais_proximo(data, len(data))
    print('Vizinho mais próximo: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    #Inserção mais barata
    t_inicio = time.time()
    tam_rota, rota, tamanhos_cidades = insercao_mais_barata(data, len(data))
    print('Inserção mais barata: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    #Opt2
    t_inicio = time.time()
    rota = n2_opt(data, rota, tam_rota)
    print('Opt2: ', rota)
    print('Tempo de execução: ', (time.time() - t_inicio))
