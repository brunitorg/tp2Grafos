# implementação dos algoritmos solicitados no TP2
import random
from itertools import permutations
import sys


def criarGrafoMatriz(vertices, pesoMin, pesoMax):
    arestas = (vertices * (vertices - 1)) / 2
    G = [[0 for i in range(vertices)] for i in range(vertices)]
    i = 0
    while i < arestas:
        u = random.randint(0, vertices - 1)
        v = random.randint(0, vertices - 1)
        if u != v and G[u][v] == 0:
            peso = random.randint(pesoMin, pesoMax)
            G[u][v] = peso
            G[v][u] = peso
            i += 1
    return G


def vizinhoMaisProximo(matriz):
    u = 0
    C = []
    #lista de vertices da matriz
    Q = [i for i in range(len(matriz))]
    Q.remove(u)
    while Q: #Enquanto há arestas para visitar
        aux = float('inf')
        v = -1
        #encontra o vizinho mais proximo
        for i in range(len(matriz)):
            if matriz[u][i] < aux and i not in C:
                aux = matriz[u][i]
                v = i
        #adiciona o vizinho ao ciclo
        C.append(v)
        if v != 0:
            Q.remove(v)
        u = v
    #adiciona o vertice origem ao ciclo
    C.append(C[0])
    #retorna ciclo hamiltoniano
    return C


def forcaBruta(matriz):
    custoMin = float('inf')
    Cbest = None
    # Faz permutação para encontrar todos os possiveis caminhos
    for C in permutations(range(len(matriz))):
        # Converte a tupla em uma lista
        C = list(C)
        # Adiciona o vertice de origem na lista para fechar o ciclo
        C.append(C[0])
        # Calcula o custo do ciclo
        custoC = recuperaCusto(C, matriz)
        # Se o custoC < custoMin = Achou um ciclo com menor custo
        if custoMin > custoC:
            custoMin = custoC
            Cbest = C
    # retorna o ciclo de menor custo
    return Cbest


def recuperaCusto(caminho, matriz):
    custo = 0
    for i in range(len(caminho)):
        if i == len(caminho) - 1:
            break
        else:
            custo += matriz[caminho[i]][caminho[i + 1]]
    return custo