from random import uniform


def gerar_numero_aleatorio():
    '''A seed para o gerador é o horario atual do sistema, vide documentação.'''
    return uniform(0, 1000)


def gerar_arquivo_de_numeros_aleatorios(quantidade_de_linhas=10, quantidade_por_linha=100):
    with open("./numeros_aleatorios.txt", "w") as arquivo:
        for _ in range(quantidade_de_linhas):
            for _ in range(quantidade_por_linha):
                arquivo.write(str(gerar_numero_aleatorio()))
                arquivo.write(" ")
            arquivo.write("\n")


gerar_arquivo_de_numeros_aleatorios()
