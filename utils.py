def calc_tam_rota(matriz, rota):
    tam_rota = 0
    for x in range(len(rota) - 1):
        tam_rota += matriz[rota[x]][rota[x + 1]]
    tam_rota += matriz[rota[-1]][rota[0]]
    return tam_rota
    