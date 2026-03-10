# Função que executa o algoritmo de Euclides em um laço de repetição
def mdc(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b


# Função que executa o algoritmo de Euclides de forma recursiva
def mdc_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)


# Benchmark para medir o tempo de execução das funções em um loop de dez milhões de operações
def benchmark():
    a, b = 1071, 462 
    for _ in range(10_000_000):
        mdc(a, b)
        mdc_recursivo(a, b)

benchmark()
