import random
import copy
from utils import *

def grasp(matriz, construtivo, busca_local, iteracoes=55, lrc=30):
    cont = 0
    tam_rota, melhor_sol = construtivo(matriz, len(matriz))
    while cont < iteracoes:
        lista_lrc = []

        for _ in range(0, lrc):
            tam_rota, rota = construtivo(matriz, len(matriz))
            lista_lrc.append(rota)
        candidato = random.randrange(0, lrc)
        rota_atual = busca_local(matriz, lista_lrc[candidato])

        if calc_tam_rota(matriz, rota_atual) < calc_tam_rota(matriz, melhor_sol):
            melhor_sol = copy.deepcopy(rota_atual)
        cont += 1
    return calc_tam_rota(matriz, melhor_sol), melhor_sol
