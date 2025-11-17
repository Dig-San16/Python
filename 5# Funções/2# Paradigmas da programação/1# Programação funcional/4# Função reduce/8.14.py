from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10] 

resultado = reduce(lambda a , b: b + a, lista) #3

print(resultado)

#A primeira linha utiliza-se do FROM e IMPORT para importar a função reduce da
#biblioteca FUNCTOOLS. 

#Na terceira linha, utiliza-se a função reduce para somar todos os elementos
#da lista. O argumento "lambda x, y: x + y" representa uma função anônima
#que recebe dois parâmetros x e y e retorna a soma deles.
#A função reduce aplica essa operação de soma cumulativa aos elementos da
#lista, resultando em um único valor. Em seguida, o valor reduzido é dividido
#pela quantidade de elementos da lista
