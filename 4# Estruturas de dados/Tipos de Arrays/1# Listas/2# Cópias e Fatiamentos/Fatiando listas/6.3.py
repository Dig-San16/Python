#Existirá certas situações onde queremos modificar o conteúdo de uma lista.
#Veja este exemplo:

L = [1,2,3,4,5]
V = L

print(V)
print(L)

#Quando trocamos a posição de determinado valor, acontece algo peculiar

V[0] = 6
print(V)
print(L)

#Ao modificar um valor na variavel V, modificamos o mesmo valor de L.
#Para que consigamos fazer uma cópia independente,
#utilizamos o método de fatiamento:

L = [1,2,3,4,5]
V = L[:] #<-- Fatiamento
V[0] = 6
print(L)
print(V)
