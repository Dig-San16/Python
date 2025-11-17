#A conversão consiste em converter as chaves e os items de um dicinário

#Uma tupla chamada artigo será convertida para diciónario para pegar as chaves
#e os valores

artigo = dict(
    titulo='Modulo 02 | Python: Estruturas de Dados',
    corpo='Topicos, Aulas, Listas, Conjuntos, Dicionários, ...',
    total_caracteres=1530
)

#As chaves são definidas por .keys

chaves = list(artigo.keys())
print(chaves)

#Os valores das chaves são definidas por .values

valores = list(artigo.values())
print(valores)
