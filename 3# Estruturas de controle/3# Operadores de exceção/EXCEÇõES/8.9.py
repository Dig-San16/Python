#As exceções são erros que ocorrem durante a execução de um código

#Exemplos:

#ZeroDivisionError: DIVIDIR NUMERO POR 0

preco = 132.85
pessoas = 0
print(preco / pessoas)



#TypeError: CONCATENAR NUMERO 

nome = 'Eneas'
idade = 89
apresentacao = 'meu nome é ' + nome + ' e eu tenho ' + idade + ' anos'
print(apresentacao)



#IndexError: INDICE INEXISTENTE


anos = [2019, 2020, 2021]

print(ano_atual = anos[3])



#KeyError: ELEMENTO INEXISTENTE

cursos = {
    'python': {
        'nome': 'Python para Análise de Dados', 'duracao': 2.5
    }, 
    'sql': {
        'nome': 'SQL para Análise de Dados', 'duracao': 2
    }
}

curso_atual = cursos['analista']
print(curso_atual)



#SyntaxError: ESCRITA INVÁLIDA

idade = 10

if idade > 10:
   print(True)

