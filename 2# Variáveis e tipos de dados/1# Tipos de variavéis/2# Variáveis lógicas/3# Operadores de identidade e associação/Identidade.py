#Os operadores de identidade são usados 
#para comparar a identidade de objetos, ou seja, para verificar
#se dois objetos referenciam exatamente o mesmo local na memória.

#Os operadores de identidade são comumente utilizados para identificar se uma variável é 'Null'

#existe dois tipos operaçoes de identificação

x = [1, 2, 3]
y = [1, 2, 3]
z = x

#'IS': Verifica se dois objetos fazem referência na memória

print(x is y) # False, porque x e y são objetos diferentes
print(x is z) # True, porque x e z referenciam o mesmo objeto


#'IS NOT': Verifica se dois objetos não fazem referência na memória

print(x is not z) # False, porque x e z referenciam o mesmo objeto
print(x is not y) # True, porque x e y são objetos diferentes


#O que faz eles se diferenciarem dos operadores '==' e '!=' é que:

#'==' e '!=' focam mais nos valores do objeto |(strings, inteiros...)

#'IS' e 'IS NOT' focam mais no objeto do que nos valores (objeto é nulo, objeto é false...)

