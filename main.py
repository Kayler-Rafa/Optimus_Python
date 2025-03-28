import time
import numpy as np
import matplotlib.pyplot as plt
from tsp_utils import carregar_instancia, construir_matriz_distancias
from simulated_annealing import tempera_simulada
from genetic_algorithm import algoritmo_genetico

# Carregar os dados da instância ATT48
arquivo_tsp = "att48.tsp"
coordenadas = carregar_instancia(arquivo_tsp)
matriz_distancias = construir_matriz_distancias(coordenadas)

# Definição dos parâmetros para os algoritmos
TEMPERATURA_INICIAL = 10000
TAXA_RESFRIAMENTO = 0.995
ITERACOES = 5000

POPULACAO_TAMANHO = 100
GERACOES = 500
TAXA_MUTACAO = 0.1

# Número de execuções
NUM_EXECUCOES = 10

melhor_solucao_sa, melhor_custo_sa = None, float("inf")
melhor_solucao_ga, melhor_custo_ga = None, float("inf")

custos_sa = []
custos_ga = []

print("Executando Têmpera Simulada e Algoritmo Genético 10 vezes...")

for i in range(NUM_EXECUCOES):
    print(f"Execução {i+1}/10...")
    
    # Executar Têmpera Simulada
    solucao_sa, custo_sa = tempera_simulada(matriz_distancias, TEMPERATURA_INICIAL, TAXA_RESFRIAMENTO, ITERACOES)
    custos_sa.append(custo_sa)
    if custo_sa < melhor_custo_sa:
        melhor_solucao_sa, melhor_custo_sa = solucao_sa, custo_sa
    
    # Executar Algoritmo Genético
    solucao_ga, custo_ga = algoritmo_genetico(matriz_distancias, POPULACAO_TAMANHO, GERACOES, TAXA_MUTACAO)
    custos_ga.append(custo_ga)
    if custo_ga < melhor_custo_ga:
        melhor_solucao_ga, melhor_custo_ga = solucao_ga, custo_ga

# Exibir resultados finais
print("\n\n--- RESULTADOS FINAIS ---")
print(f"Melhor solução Têmpera Simulada: {melhor_solucao_sa}")
print(f"Custo da melhor solução SA: {melhor_custo_sa}")
print("\n")
print(f"Melhor solução Algoritmo Genético: {melhor_solucao_ga}")
print(f"Custo da melhor solução GA: {melhor_custo_ga}")

# Gerar gráficos
plt.figure(figsize=(10,5))
plt.plot(range(1, NUM_EXECUCOES+1), custos_sa, marker='o', label='Têmpera Simulada')
plt.plot(range(1, NUM_EXECUCOES+1), custos_ga, marker='s', label='Algoritmo Genético')
plt.xlabel("Execução")
plt.ylabel("Custo da solução")
plt.title("Comparação dos custos das soluções")
plt.legend()
plt.grid()
plt.show()
