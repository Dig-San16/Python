#para pesquisar se uma string está dentro de outra e obter a posição da primeira
#ocorrencia, voce pode utilizar o método FIND.

s = "Olá mundo"

u = s.find('mun')

d = s.find('ok')

print(u)
print(d)

#caso o objetivo for para pesquisar da direita para esquerda, utiliza-se
#o método RFIND.

y = "um dia de sol"

t = y.rfind('d')
q = y.find('d')

print(t)
print(q)

#Tanto FIND quanto RFIND suportam voce especificar o inicio(start) e o fim(end).

c = 'uma cambalhota, duas cambalhotas, tres cambalhotas'

e = c.find('cambalhotas')

e1 = c.rfind('cambalhotas')

e2 = c.find('cambalhotas', 7)

e3 = c.find('cambalhotas', 30)

e4 = c.find('cambalhotas', 0, 10)

print(e)
print(e1)
print(e2)
print(e3)
print(e4)


