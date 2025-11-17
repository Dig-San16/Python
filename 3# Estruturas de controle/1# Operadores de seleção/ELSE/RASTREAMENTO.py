#O RASTREAMENTO serve para entendermos o que cada linha do programa significa
#e os efeitos que ela produz, essa técnica é extremamente importante para
#impedir erros relacionados a "espaçamento", portanto, siga esse exemplo bobo
#abaixo, para que no fim, voce começe a rastrear utilizando lápis e borracha.

categoria = int(input("digite de 1 a 5: ")) #preparador
if categoria == 1: #preparador
       linhas = 10  
else: #preparador
    if categoria == 2: #executor
           linhas = 18
    else: #executor
        if categoria == 3:#caixista
               linhas = 23
        else: #executor
            if categoria == 4: #caxista
                   linhas = 26
            else: #executor
                if categoria == 5: #caixista
                       linhas = 31
                else: #executor
                    print("categoria invalida, tu é cego?! digite de 1 a 5!") #caixista
print(f"o preço será: R${linhas:.2f}") #preparador
                    
#preparador: ele fica no inicio e no fim, e constantemente é o que inicia
#o programa

#executor: esta dentro do preparador. fica alinhado entre as duas pontas do
#preparador

#caixista: esta dentro do executor. fica alinhado entre as duas pontas
#do executor
