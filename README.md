# Otimização do Problema do Caixeiro Viajante (TSP)

Este projeto implementa a solução para o **Problema do Caixeiro Viajante (TSP)** utilizando dois métodos de otimização:

- **Têmpera Simulada** (Simulated Annealing)
- **Algoritmo Genético**

O objetivo é encontrar o menor percurso possível que visita todas as cidades de uma instância do TSP e retorna ao ponto de origem.

## 📌 Métodos Utilizados

### 🔥 Têmpera Simulada
A Têmpera Simulada é uma técnica de otimização baseada no processo de resfriamento de metais. Ela permite aceitar soluções piores temporariamente para escapar de mínimos locais. Os parâmetros utilizados foram:
- **Temperatura Inicial**: 10.000
- **Taxa de Resfriamento**: 0.995
- **Número de Iterações**: 5.000

### 🧬 Algoritmo Genético
O Algoritmo Genético é inspirado na seleção natural e opera através de processos de seleção, cruzamento e mutação para evoluir soluções melhores ao longo do tempo. Os parâmetros utilizados foram:
- **Tamanho da População**: 100
- **Número de Gerações**: 500
- **Taxa de Mutação**: 10%

## 📂 Estrutura do Projeto

```
TSP_Optimization/
│── main.py                    # Código principal que executa os algoritmos
│── tsp_utils.py                # Funções auxiliares para manipulação de dados
│── simulated_annealing.py      # Implementação da Têmpera Simulada
│── genetic_algorithm.py        # Implementação do Algoritmo Genético
│── att48.tsp                   # Instância do problema (dados das cidades)
│── README.md                   # Documentação do projeto
```

## 🚀 Como Rodar o Projeto

### 📌 Pré-requisitos
Certifique-se de ter o **Python 3.10+** instalado e os pacotes necessários:
```bash
pip install numpy matplotlib
```

### ▶️ Executando o Código
1. Clone o repositório ou baixe os arquivos.
2. No terminal, execute:
   ```bash
   python main.py
   ```
3. O código executará **10 vezes** cada algoritmo e exibirá o **melhor resultado** de cada um.
4. Ao final, um **gráfico comparativo** será gerado.

## 📊 Resultados
O código compara os dois métodos e exibe um **gráfico com os custos das soluções** em cada execução. Isso permite analisar o desempenho de cada técnica.

---

Se houver dúvidas ou sugestões, sinta-se à vontade para contribuir! 🚀
