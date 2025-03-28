import math
import numpy as np
import random

def calcular_distancia(ponto1, ponto2):
    """Calcula a distância euclidiana entre dois pontos."""
    return math.sqrt((ponto1[0] - ponto2[0])**2 + (ponto1[1] - ponto2[1])**2)

def carregar_instancia(nome_arquivo):
    """Carrega as coordenadas das cidades a partir do arquivo .tsp"""
    with open(nome_arquivo, 'r') as f:
        linhas = f.readlines()

    coordenadas = []
    inicio_dados = False
    for linha in linhas:
        if inicio_dados:
            partes = linha.strip().split()
            if len(partes) == 3:
                _, x, y = partes
                coordenadas.append((float(x), float(y)))
        elif linha.startswith('NODE_COORD_SECTION'):
            inicio_dados = True
    
    return coordenadas

def construir_matriz_distancias(coordenadas):
    """Cria uma matriz de distâncias entre todas as cidades."""
    n = len(coordenadas)
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                matriz[i][j] = calcular_distancia(coordenadas[i], coordenadas[j])
    return matriz

def calcular_custo(solucao, matriz):
    """Calcula o custo total de uma solução (percurso)."""
    custo = 0
    for i in range(len(solucao)):
        custo += matriz[solucao[i-1]][solucao[i]]
    return custo

def gerar_vizinho(solucao):
    """Gera uma solução vizinha trocando duas cidades de posição."""
    a, b = random.sample(range(len(solucao)), 2)
    solucao_vizinha = solucao[:]
    solucao_vizinha[a], solucao_vizinha[b] = solucao_vizinha[b], solucao_vizinha[a]
    return solucao_vizinha
