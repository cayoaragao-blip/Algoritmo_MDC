# Aplicação do algoritmo de Euclides para calcular o MDC (Máximo Divisor Comum) entre dois números


# Atribuição de valores
a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))


# Função que executa o algoritmo de Euclides em um laço de repetição
def mdc(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b

# Função que executa o algoritmo de Euclides de modo recursivo
def mdc_recursivo(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)

# Chamando a função e imprimindo o resultado no terminal
resultado = mdc(a, b)
print(f"O MDC destes números é {resultado}") 

        
