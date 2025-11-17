#GET é usado para obter um valor associado a uma chave específica.

#Fórmula: get(chave, valor_padrao)

dicionario = {'nome': 'Alice', 
              'idade': 25}

nome = dicionario.get('nome', 'Desconhecida')
idade = dicionario.get('idade', 'Desconhecida')
cidade = dicionario.get('cidade', 'Desconhecida')

print(nome)  
print(idade)   
print(cidade)   

#No método get() é possível a adição de mais um valor (valor_padrao),
#isso é útil para evitar exceções quando você não tem certeza se uma chave
#existe no dicionário.
