import random
import copy

def calc_tam_rota2(matriz, rota):
    tam_rota = 0
    for x in range(len(rota) - 1):
        tam_rota += matriz[rota[x]][rota[x + 1]]
    tam_rota += matriz[rota[-1]][rota[0]]
    return tam_rota

#TODO: Melhorar aleatoriedade
def grasp(matriz, construtivo, busca_local, iteracoes=55, lrc=25, alpha=0.5):
    cont = 0
    tam_rota, melhor_sol = construtivo(matriz, len(matriz))
    while cont < iteracoes:
        lista_lrc = []

        for _ in range(0, lrc):
            tam_rota, rota = construtivo(matriz, len(matriz))
            lista_lrc.append(rota)
        candidato = random.randrange(0, lrc-1)
        rota_atual = busca_local(matriz, lista_lrc[candidato])

        if calc_tam_rota2(matriz, rota_atual) < calc_tam_rota2(matriz, melhor_sol):
            melhor_sol = copy.deepcopy(rota_atual)
        cont += 1
    return calc_tam_rota2(matriz, melhor_sol), melhor_sol
