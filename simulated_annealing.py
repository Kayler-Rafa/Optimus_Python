import random
import math
from tsp_utils import calcular_custo, gerar_vizinho  

def tempera_simulada(matriz, temperatura_inicial, taxa_resfriamento, iteracoes):
    """Executa o algoritmo de Têmpera Simulada para encontrar um bom percurso."""
    solucao_atual = list(range(len(matriz)))
    random.shuffle(solucao_atual)
    custo_atual = calcular_custo(solucao_atual, matriz)
    melhor_solucao = solucao_atual[:]
    melhor_custo = custo_atual
    
    temperatura = temperatura_inicial
    
    for _ in range(iteracoes):
        solucao_vizinha = gerar_vizinho(solucao_atual)
        custo_vizinho = calcular_custo(solucao_vizinha, matriz)
        
        delta = custo_vizinho - custo_atual
        
        if delta < 0 or random.random() < math.exp(-delta / temperatura):
            solucao_atual = solucao_vizinha
            custo_atual = custo_vizinho
            
            if custo_atual < melhor_custo:
                melhor_solucao = solucao_atual[:]
                melhor_custo = custo_atual
        
        temperatura *= taxa_resfriamento
    
    return melhor_solucao, melhor_custo
