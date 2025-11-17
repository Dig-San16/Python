numero_e_par = lambda numero: True if numero % 2 == 0 else False #1

numeros = range(0, 10)

for numero in numeros:
  if numero_e_par(numero) == True:
    print(f'O número {numero} é par!')

#A função lambda aceita um parâmetro chamado numero.
    
#TRUE indica o valor a retornar se a condição for verdadeira.

#numero % 2 == 0, que verifica se o número é divisível por 2
#(ou seja, se é par).

#FALSE indica o valor retornado se a condição for falsa.


#FATO:
#A primeira linha do código é equivalente a uma função com a seguinte definição:

def numero_e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
