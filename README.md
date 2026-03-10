# Algoritmo de Euclides: 
Este projeto tem como finalidade aprensentar dois tipos de funções que executam de forma eficiente o algoritmo de Euclides, cuja função é encontrar o MDC (máximo divisor comum) entre dois números. Somado a isto, é implementado um sistema de benchmark para avaliar qual dos dois métodos é mais rápido em larga escala (milhões de operações).

🛠️ Tecnologias e Conceitos: 
Python 3.x e Lógica Matemática - Algoritmo de Euclides📋

Pré-requisitos:
Python instalado;
Git;
Gerenciador de pacotes (pip);

## Benchmark
Para comparar as implementações, foi utilizado o cProfile isolando a lógica de negócio em um loop de 10 milhões de iterações.

Algoritmo,Calls,Tottime (s),Cumtime (s)
Iterativo,20M,1.862,1.862
Recursivo,10M,1.294,2.078

Metodologia: O script benchmark.py foi executado em Python 3.x sem interações de I/O.

## Como rodar o benchmark:
python -m cProfile Algoritmo_MDC.py