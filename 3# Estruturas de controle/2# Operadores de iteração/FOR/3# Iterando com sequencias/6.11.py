#Em dicionários, a estrutura permite a execução de um bloco de código para
#todos os elementos de um dicionário, utiliza-se de alguns métodos.

credito = {'123': 750, '456': 812, '789': 980}

#ITEMS
for chave, valor in credito.items():
  print(f'Para o documento {chave}, o valor do escore de crédito é {valor}.')

print('\n')

#KEYS
for chave in credito.keys():
  print(f'Para o documento {chave}, o valor do escore de crédito é {credito[chave]}.')

print('\n')

#VALUES
for valor in credito.values():
  print(f'O valor do escore de crédito é {valor}, mas não temos mais as chaves ')

print('\n')

