# ------------------------------------------------------------
# Gerador de números aleatórios, Metaheurísticas
# Dupla: Tamara D. Carvalho, Luan P. Cunha.
#
# Para executar o programa, execute a seguinte linha de comando no terminal:
# python pseudo-random_numbers_generator.py
#
# Será criado o arquivo numeros_aleatorios.txt com 10 linhas, sendo cada uma com 100 números inteiros
#
# Repositório no github: https://github.com/LuanPCunha/meta-heristica
# ------------------------------------------------------------

from random import randint


def gerar_numero_aleatorio():
    '''A seed para o gerador é o horario atual do sistema, vide documentação.'''
    return randint(0, 1000)


def gerar_arquivo_de_numeros_aleatorios(quantidade_de_linhas=10, quantidade_por_linha=100):
    with open("./numeros_aleatorios.txt", "w") as arquivo:
        for _ in range(quantidade_de_linhas):
            for _ in range(quantidade_por_linha):
                arquivo.write(str(gerar_numero_aleatorio()))
                arquivo.write(" ")
            arquivo.write("\n")


gerar_arquivo_de_numeros_aleatorios()
