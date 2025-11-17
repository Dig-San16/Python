# Função de condição para verificar se um número é par
def verificar_par(numero):
    return numero % 2 == 0

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando filter para obter apenas os números pares
numeros_pares = list(filter(verificar_par, numeros))

# Exibindo o resultado
print(numeros_pares)

