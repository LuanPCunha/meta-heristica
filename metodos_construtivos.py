import math
from random import randrange

def vizinho(matriz, rota, cidade):
    cidade_vizinha = cidade
    distancias = matriz[cidade]
    min_dist = math.inf
    for i in range(len(distancias)):
        if distancias[i] < min_dist and i not in rota:
            min_dist = distancias[i]
            cidade_vizinha = i
    return cidade_vizinha, min_dist


def vizinho_mais_proximo(matriz, qtd_cidades):
    cidade = randrange(0, qtd_cidades-1)
    atual, rota, tam_rota, tamanhos_cidades = cidade, [cidade], 0, []
    while len(rota) < qtd_cidades:
        cidade_vizinha, dist = vizinho(matriz, rota, atual)
        tam_rota += dist
        tamanhos_cidades.append(dist)
        rota.append(cidade_vizinha)
        atual = cidade_vizinha
    tam_rota += matriz[atual][cidade]
    tamanhos_cidades.append(matriz[atual][cidade])
    rota.append(cidade)
    return tam_rota, rota, tamanhos_cidades



def insercao_minima(matriz, rota):
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


def insercao_mais_barata(matriz, qtd_cidades):
    cidade = randrange(0, qtd_cidades-1)
    rota, tamanhos_cidades = [cidade], []
    cidade_vizinha, dist = vizinho(matriz, rota, cidade)
    tam_rota = dist
    tamanhos_cidades.append(dist)
    rota.append(cidade_vizinha)
    while len(rota) < qtd_cidades:
        dist, rota = insercao_minima(matriz, rota)
        tam_rota += dist
        tamanhos_cidades.append(dist)
    tam_rota += matriz[rota[-1]][rota[0]]
    tamanhos_cidades.append(matriz[rota[-1]][rota[0]])
    return tam_rota, rota, tamanhos_cidades
