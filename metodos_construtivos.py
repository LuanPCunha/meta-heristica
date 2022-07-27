import math
from random import randrange
from utils import *


def add_aleatorio1(matriz, rota):
    aleatorio = randrange(0, 100)
    if aleatorio < len(matriz) and aleatorio not in rota:
        return True, aleatorio, matriz[(rota[-1])][aleatorio]
    else:
        return False, 0, 0

def vizinho(matriz, rota, cidade, maisAleatorio=True):
    sucesso, aleatorio, tam = add_aleatorio1(matriz, rota)
    if sucesso and maisAleatorio:
        return aleatorio, tam
    cidade_vizinha = cidade
    distancias = matriz[cidade]
    min_dist = math.inf
    for i in range(len(distancias)):
        if distancias[i] < min_dist and i not in rota:
            min_dist = distancias[i]
            cidade_vizinha = i
    return cidade_vizinha, min_dist


def vizinho_mais_proximo(matriz, qtd_cidades, maisAleatorio=True):
    cidade = randrange(0, qtd_cidades)
    atual, rota, tam_rota, tamanhos_cidades = cidade, [cidade], 0, []
    while len(rota) < qtd_cidades:
        cidade_vizinha, dist = vizinho(matriz, rota, atual, maisAleatorio)
        tam_rota += dist
        tamanhos_cidades.append(dist)
        rota.append(cidade_vizinha)
        atual = cidade_vizinha
    tam_rota += matriz[atual][cidade]
    tamanhos_cidades.append(matriz[atual][cidade])
    return tam_rota, rota

#------------------------------------------------------------------------------------------
def add_aleatorio2(matriz, rota):
    aleatorio = randrange(0, 100)
    if aleatorio < len(matriz) and aleatorio not in rota:
        nova_rota = rota + [aleatorio]
        return True, nova_rota, matriz[(rota[-1])][aleatorio]
    else:
        return False, rota, 0

def insercao_minima(matriz, rota, maisAleatorio=True):
    sucesso, rota_elemento_aleatorio, tam = add_aleatorio2(matriz, rota)
    if sucesso and maisAleatorio:
        return tam, rota_elemento_aleatorio

    melhor_dist, nova_rota = float('inf'), None
    for cidade in range(len(matriz)):
        if cidade in rota:
            continue
        for index in range(len(rota) - 1):
            i = rota[index]
            j = rota[index + 1]
            k = cidade
            # dik + dkj - dij
            dist = matriz[i][k] + matriz[k][j] - matriz[i][j]
            if dist < melhor_dist:
                melhor_dist = dist
                nova_rota = rota[:index + 1] + [cidade] + rota[index + 1:]
    return melhor_dist, nova_rota


def insercao_mais_barata(matriz, qtd_cidades, maisAleatorio=True):
    cidade = randrange(0, qtd_cidades)
    rota, tamanhos_cidades = [cidade], []
    cidade_vizinha, dist = vizinho(matriz, rota, cidade)
    tam_rota = dist
    tamanhos_cidades.append(dist)
    rota.append(cidade_vizinha)
    while len(rota) < qtd_cidades:
        dist, rota = insercao_minima(matriz, rota, maisAleatorio)
        tam_rota += dist
        tamanhos_cidades.append(dist)
    tam_rota += matriz[rota[-1]][rota[0]]
    tamanhos_cidades.append(matriz[rota[-1]][rota[0]])
    return tam_rota, rota
