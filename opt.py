def calc_tam_rota(matriz, rota):
    tam_rota = 0
    for x in range(len(rota) - 1):
        tam_rota += matriz[rota[x]][rota[x + 1]]
    tam_rota += matriz[rota[-1]][rota[0]]
    return tam_rota


def n2_opt(matriz, rota, tam_rota):
    estavel, melhor_tam, melhor_rota = False, tam_rota, rota
    while not estavel:
        estavel = True
        for i in range(1, len(matriz) - 1):
            for j in range(i + 1, len(matriz)):
                candidato = melhor_rota[:i] + melhor_rota[i:j + 1][::-1] + melhor_rota[j + 1:]
                tam_candidato = calc_tam_rota(matriz, candidato)
                if tam_candidato < melhor_tam:
                    estavel = False
                    melhor_rota, melhor_tam = candidato, tam_candidato  
    return melhor_rota

