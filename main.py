import time
import math

from metodos_construtivos import *
from opt import *
from grasp import *

arq, tam_otm = "data_TSP/att48_d.txt", 33523
#arq, tam_otm = "data_TSP/dantzig42_d.txt", 699
#arq, tam_otm = "data_TSP/fri26_d.txt", 937
#arq, tam_otm = "data_TSP/gr17_d.txt", 2085
#arq, tam_otm = "data_TSP/p01_d.txt", 291
#arq, tam_otm = "data_TSP/five_d.txt", 19


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
    # Carregar dados
    matriz = ler_arquivo()
    inf_para_distancia_zero(matriz)
    # print(matriz)

    print("Valor ótimo:", tam_otm)

    # Vizinho mais próximo
    t_inicio = time.time()
    print()
    tam_rota, rota = vizinho_mais_proximo(matriz, len(matriz))
    print('Vizinho mais próximo: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    # Inserção mais barata
    t_inicio = time.time()
    print()
    tam_rota, rota = insercao_mais_barata(matriz, len(matriz))
    print('Inserção mais barata: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    # Opt2
    t_inicio = time.time()
    print()
    rota = n2_opt(matriz, rota)
    print('Opt2: ', rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    # Opt3
    t_inicio = time.time()
    print()
    rota = n3_opt(matriz, rota)
    print('Opt3: ', rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    #------------------   Grasp   -------------------------

    t_inicio = time.time()
    print()
    tam_rota, rota = grasp(matriz, vizinho_mais_proximo, n2_opt)
    print('Vizinho_mais_proximo+n2_opt: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    t_inicio = time.time()
    print()
    tam_rota, rota = grasp(matriz, vizinho_mais_proximo, n3_opt)
    print('Vizinho_mais_proximo+n3_opt: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    t_inicio = time.time()
    print()
    tam_rota, rota = grasp(matriz, insercao_mais_barata, n2_opt)
    print('insercao_mais_barata+n2_opt: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))

    t_inicio = time.time()
    print()
    tam_rota, rota = grasp(matriz, insercao_mais_barata, n3_opt)
    print('insercao_mais_barata+n3_opt: ', tam_rota, rota)
    print('Tempo de execução: ', (time.time() - t_inicio))
