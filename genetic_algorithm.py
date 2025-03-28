import random
from tsp_utils import calcular_custo

def criar_populacao(tamanho_populacao, num_cidades):
    """Cria uma população inicial de soluções aleatórias."""
    populacao = []
    for _ in range(tamanho_populacao):
        individuo = list(range(num_cidades))
        random.shuffle(individuo)
        populacao.append(individuo)
    return populacao

def avaliar_populacao(populacao, matriz):
    """Avalia cada indivíduo da população e retorna (indivíduo, custo)."""
    return [(individuo, calcular_custo(individuo, matriz)) for individuo in populacao]

def selecionar_pais(avaliacoes):
    """Seleciona dois pais usando torneio (seleciona os melhores)."""
    torneio = random.sample(avaliacoes, 5)
    torneio.sort(key=lambda x: x[1])
    return torneio[0][0], torneio[1][0]

def crossover(pai1, pai2):
    """Realiza o cruzamento entre dois pais para gerar um filho."""
    corte = random.randint(1, len(pai1) - 2)
    filho = pai1[:corte] + [gene for gene in pai2 if gene not in pai1[:corte]]
    return filho

def mutacao(individuo, taxa_mutacao):
    """Realiza mutação trocando dois genes."""
    if random.random() < taxa_mutacao:
        a, b = random.sample(range(len(individuo)), 2)
        individuo[a], individuo[b] = individuo[b], individuo[a]

def algoritmo_genetico(matriz, tamanho_populacao, geracoes, taxa_mutacao):
    """Executa o Algoritmo Genético."""
    num_cidades = len(matriz)
    populacao = criar_populacao(tamanho_populacao, num_cidades)

    for _ in range(geracoes):
        avaliacoes = avaliar_populacao(populacao, matriz)
        nova_populacao = []

        for _ in range(tamanho_populacao // 2):
            pai1, pai2 = selecionar_pais(avaliacoes)
            filho1, filho2 = crossover(pai1, pai2), crossover(pai2, pai1)
            mutacao(filho1, taxa_mutacao)
            mutacao(filho2, taxa_mutacao)
            nova_populacao.extend([filho1, filho2])

        populacao = nova_populacao

    melhor_solucao, melhor_custo = min(avaliacoes, key=lambda x: x[1])
    return melhor_solucao, melhor_custo
