#POP nos dicionários Remove a chave especificada e retorna o valor associado
#a ela. Se a chave não existir, retorna o
#valor padrão ou gera um erro se nenhum valor padrão for fornecido.

#Fórmula: pop(chave, valor_padrao)

meu_dict = {'fruta': 'maçã', 'cor': 'verde', 'sabor': 'azedo'}
sabor = meu_dict.pop('sabor', 'desconhecido')
print(sabor)

#caso uma chave não existir, o valor padrão será colocado para complementar.

nomeCie = meu_dict.pop('nome_cientifico', 'desconhecido')
print(nomeCie)
