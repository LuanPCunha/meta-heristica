from itertools import cycle, islice, dropwhile
import numpy as np


def calc_tam_rota(matriz, rota):
    tam_rota = 0
    for x in range(len(rota) - 1):
        tam_rota += matriz[rota[x]][rota[x + 1]]
    tam_rota += matriz[rota[-1]][rota[0]]
    return tam_rota


def n2_opt(matriz, rota):
    estavel, melhor_tam, melhor_rota = False, calc_tam_rota(matriz, rota), rota
    while not estavel:
        estavel = True
        for i in range(1, len(matriz) - 1):
            for j in range(i + 1, len(matriz)):
                candidato = melhor_rota[:i] + \
                    melhor_rota[i:j + 1][::-1] + melhor_rota[j + 1:]
                tam_candidato = calc_tam_rota(matriz, candidato)
                if tam_candidato < melhor_tam:
                    estavel = False
                    melhor_rota, melhor_tam = candidato, tam_candidato
    return melhor_rota


def n3_opt(matriz, rota):
    matriz = np.array(matriz)
    custo_dos_movimentos = {"opt_caso_1": 0, "opt_caso_2": 0,
                            "opt_caso_3": 0, "opt_caso_4": 0, "opt_caso_5": 0,
                            "opt_caso_6": 0, "opt_caso_7": 0, "opt_caso_8": 0}
    melhorou = True
    melhor_rota_encontrada = rota
    while melhorou:
        melhorou = False
        for (i, j, k) in possiveis_segmentos(len(matriz)):

            for opt_caso in list(custo_dos_movimentos.keys()):
                custo_dos_movimentos[opt_caso] = obter_alteração_de_custo_da_solução(
                    matriz, melhor_rota_encontrada, opt_caso, i, j, k)

            melhor_retorno = max(custo_dos_movimentos,
                                 key=custo_dos_movimentos.get)
            if custo_dos_movimentos[melhor_retorno] > 0:
                melhor_rota_encontrada = inverter_segmentos(
                    melhor_rota_encontrada, melhor_retorno, i, j, k)
                melhorou = True
                break

    cycled = cycle(melhor_rota_encontrada)
    skipped = dropwhile(lambda x: x != 0, cycled)
    sliced = islice(skipped, None, len(melhor_rota_encontrada))
    melhor_rota_encontrada = list(sliced)
    return melhor_rota_encontrada


def possiveis_segmentos(N):
    segmentos = ((i, j, k) for i in range(N) for j in range(i + 2, N-1)
                 for k in range(j + 2, N - 1 + (i > 0)))
    return segmentos


def obter_alteração_de_custo_da_solução(matriz, rota, caso, i, j, k):
    A, B, C, D, E, F = rota[i - 1], rota[i], rota[j -
                                                  1], rota[j], rota[k - 1], rota[k % len(rota)]
    if caso == "opt_caso_1":
        return 0
    elif caso == "opt_caso_2":
        return matriz[A, B] + matriz[E, F] - (matriz[B, F] + matriz[A, E])
    elif caso == "opt_caso_3":
        return matriz[C, D] + matriz[E, F] - (matriz[D, F] + matriz[C, E])
    elif caso == "opt_caso_4":
        return matriz[A, B] + matriz[C, D] + matriz[E, F] - (matriz[A, D] + matriz[B, F] + matriz[E, C])
    elif caso == "opt_caso_5":
        return matriz[A, B] + matriz[C, D] + matriz[E, F] - (matriz[C, F] + matriz[B, D] + matriz[E, A])
    elif caso == "opt_caso_6":
        return matriz[B, A] + matriz[D, C] - (matriz[C, A] + matriz[B, D])
    elif caso == "opt_caso_7":
        return matriz[A, B] + matriz[C, D] + matriz[E, F] - (matriz[B, E] + matriz[D, F] + matriz[C, A])
    elif caso == "opt_caso_8":
        return matriz[A, B] + matriz[C, D] + matriz[E, F] - (matriz[A, D] + matriz[C, F] + matriz[B, E])


def inverter_segmentos(rota, caso, i, j, k):

    if (i - 1) < (k % len(rota)):
        primeiro_segmento = rota[k % len(rota):] + rota[:i]
    else:
        primeiro_segmento = rota[k % len(rota):i]
    segundo_segmento = rota[i:j]
    terceiro_segmento = rota[j:k]

    if caso == "opt_caso_1":
        pass
    elif caso == "opt_caso_2":
        solucao = list(reversed(primeiro_segmento)) + \
            segundo_segmento + terceiro_segmento
    elif caso == "opt_caso_3":
        solucao = primeiro_segmento + segundo_segmento + \
            list(reversed(terceiro_segmento))
    elif caso == "opt_caso_4":
        solucao = list(reversed(primeiro_segmento)) + \
            segundo_segmento + list(reversed(terceiro_segmento))
    elif caso == "opt_caso_5":
        solucao = list(reversed(primeiro_segmento)) + \
            list(reversed(segundo_segmento)) + terceiro_segmento
    elif caso == "opt_caso_6":
        solucao = primeiro_segmento + \
            list(reversed(segundo_segmento)) + terceiro_segmento
    elif caso == "opt_caso_7":
        solucao = primeiro_segmento + \
            list(reversed(segundo_segmento)) + \
            list(reversed(terceiro_segmento))
    elif caso == "opt_caso_8":
        solucao = list(reversed(primeiro_segmento)) + \
            list(reversed(segundo_segmento)) + \
            list(reversed(terceiro_segmento))
    return solucao
