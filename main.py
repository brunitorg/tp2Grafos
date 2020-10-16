import grafo
import time


print('Grafo:')
graph = grafo.criarGrafoMatriz(5, 1, 9)

for i in range(len(graph)):
    print(graph[i])
print()

option = int(input("Algoritmo: \n\t1 Guloso\n\t2 Forca Bruta\n"))

print()
print('Processando...')
print()

inicio = time.time()
if option == 1:
    path = grafo.vizinhoMaisProximo(graph)
    fim = time.time()
    print(f'Caminho: {path}')
    print(f'Custo do Caminho: {grafo.recuperaCusto(path,graph)}')
    print(f'Tempo: {fim - inicio}')
if option == 2:
    path = grafo.forcaBruta(graph)
    fim = time.time()
    print(f'Caminho: {path}')
    print(f'Custo do Caminho: {grafo.recuperaCusto(path,graph)}')
    print(f'Tempo: {fim - inicio}')
