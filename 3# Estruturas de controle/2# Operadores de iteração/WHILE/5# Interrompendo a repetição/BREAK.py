#A função BREAK interrompe uma repetição independentemente do valor atual da
#sua condição

n = 0
while True: #1
    v = int(input("digite um número a somar ou 0 para sair: "))
    if v == 0:
        break #2
    n += v #3
print(n)

#Na primeira linha, sabe se que a estrutura é constante e irá repetir
#infinitamente, pois o valor de sua condição é verdadeiro (TRUE).

#Na segunda linha, a função BREAK só será ativada se o usuário escrever 0,
#caso for o contrário, a linha 3 será executada e a repetição continuará.
