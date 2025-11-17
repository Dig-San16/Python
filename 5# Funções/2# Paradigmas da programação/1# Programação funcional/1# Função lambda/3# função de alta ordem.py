#Uma função de alta ordem é aquela que recebe uma ou mais funções como
#argumentos e/ou retorna uma função como resultado.

def retorno(juros: float): #1
    return lambda investimento: investimento * (1 + juros) #2

retorno_5_porcento = retorno(juros=0.05) #3 
retorno_10_porcento = retorno(juros=0.10) #4

valor_final = retorno_5_porcento(investimento=1000)
print(valor_final)

valor_final = retorno_10_porcento(investimento=1000)
print(valor_final)

#Na segunda linha, a função RETURN é uma função de alta ordem,
#porque ela retorna uma função (a função lambda) com base no parâmetro juros.
#Em outras palavras, ela manipula ou opera em funções, tornando-se uma função
#de ordem superior.

#Ao chamar retorno(juros=0.05), você obtém uma função específica
#retorno_5_porcento, que, quando chamada com um valor de investimento,
#calcula o valor final com uma taxa de juros de 5%. Da mesma forma,
#retorno(juros=0.10) retorna retorno_10_porcento, que calcula o valor final
#com uma taxa de juros de 10%.
