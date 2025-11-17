#As funções READ e READLINE são usadas para ler
#dados de um arquivo aberto em Python. 

#READ: é responsável por ler todo o arquivo

with open('carros.py', 'r') as arquivo:
    conteudo = arquivo.read()
    
print(conteudo)


#READLINE: é responsável por ler o arquivo uma linha por vez

conteúdo2 = []

with open('carros.py', 'r') as arquivo:
    linha = arquivo.readline() #le a primeira linha
    while linha:
        conteúdo2.append(linha)
        linha = arquivo.readline() #le uma nova linha
    

print(conteúdo2)
    
    

