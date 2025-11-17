#O ACUMULADOR, diferentemente do contador, adiciona valores de forma
#Variável, ou seja, o número que o usuário digitar varia:

n = 1
soma = 0 
while n <= 10:
    x = int(input(f"digite o numero {n}: "))
    soma = soma + x #1
    n = n + 1 #2
print(f"Soma: {soma}")

#Dentro da estrutura de repetição, a variável soma acumulará o número que o 
#usuário digitar, ou seja, a primeira linha é um acumulador

#No segundo, está o CONTADOR que receberá 1 enquanto o usuário digitar
#um número.
