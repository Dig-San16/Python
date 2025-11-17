#IMPORT é utilizado para incluir funcionalidades de outros módulos ou
#pacotes no código.

import random

escolha = random.choice([1,2,3])
print(escolha)

#random() – retorna um número de ponto flutuante aleatório entre 0 e 1.
#randint(a, b) – retorna um número inteiro aleatório entre a e b, inclusive.
#uniform(a, b) – retorna um número de ponto flutuante aleatório entre a e b.
#choice(seq) – retorna um elemento aleatório da sequência seq.
#shuffle(seq) – embaralha aleatoriamente a sequência seq.
#sample(seq, k) – retorna uma lista de k elementos aleatórios da sequência seq.

import math

potencia = math.pow(10, 2) 
print(potencia)

#FROM é usado em conjunto com IMPORT para importar especificamente certos
#elementos de um módulo ou acessar um pacote que possui determinado módulo. 

from time import sleep

print("aguarde por favor...")
a = sleep(5)

from datetime import datetime as dt

print(dt.now())

print(dt.now().day)

print(dt.now().year)

#Cada módulo possui suas funções. Python possui inúmeros módulos para ser
#utlizados, acesse esse site para mais informações:

# https://docs.python.org/3/py-modindex.html
