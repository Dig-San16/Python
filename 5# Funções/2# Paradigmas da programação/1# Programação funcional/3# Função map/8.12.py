# Função que dobra um número
def dobrar(numero):
    return numero * 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando map para dobrar cada número na lista
resultados = list(map(dobrar, numeros))

# Exibindo o resultado
print(resultados)
