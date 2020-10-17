# iniciar aplicação
import funcoes
import sys
import time

# Recebe valores para criar grafo
vertices = int(input("Número de vértices: "))
pesoMin = int(input("Peso mínimo das arestas: "))
pesoMax = int(input("Peso máxima das arestas: "))
if vertices <= 0 or pesoMin <= 0 or pesoMax <= 0:
    sys.exit("Valores devem ser maiores que 0!")

imprimir = int(input("Deseja imprimir o grafo? 1 - Sim // 0 - Não: "))

# Recebe o algoritmo a ser usado
algoritmo = int(input("Escolha o Algoritmo:\n  1 - Vizinho Mais Próximo\n  2 - Força-Bruta\n"))
if algoritmo <= 0 or algoritmo > 2:
    sys.exit("Algoritmo inválido!")

print("Processando...")

if algoritmo == 1:
    graph = funcoes.criarGrafoMatriz(vertices, pesoMin, pesoMax)
    if imprimir == 1:
        print(graph)
    print("---------------Algoritmo Guloso do Vizinho Mais Próximo---------------")
    tempo = time.time()
    ciclo = funcoes.vizinhoMaisProximo(graph)
    tempo = time.time() - tempo
    custo = funcoes.recuperaCusto(ciclo,graph)
    print("Rota: ", ciclo, "\nCusto: ", custo, "\nTempo: ", tempo)

else:
    graph = funcoes.criarGrafoMatriz(vertices, pesoMin, pesoMax)
    if imprimir == 1:
        print(graph)
    print("---------------Algoritmo de Força-Bruta---------------")
    tempo = time.time()
    ciclo = funcoes.forcaBruta(graph)
    tempo = time.time() - tempo
    custo = funcoes.recuperaCusto(ciclo,graph)
    print("Rota: ", ciclo, "\nCusto: ", custo, "\nTempo: ", tempo)

print(":----------------Obrigado----------------: ")
