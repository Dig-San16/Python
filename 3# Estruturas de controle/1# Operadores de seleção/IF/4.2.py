velocidade = int(input("qual foi a velocidade?: "))
if velocidade > 80: #1
    
    multa = (velocidade - 80) * 5 #2
    
    print(f"Multado!, vc vai pagar em R$ {multa:.2f}") #3
    
if velocidade <= 80: #4
    
    print("boa viagem") #5

#IF é uma função que avalia uma condição, seja ela verdadeira ou falsa

#se 1 for verdadeiro, o programa executa o 1, 2 e 3 e ignora o 4 

#caso 4 for verdadeiro, o programa vai executar o 1, 4 e 5 e ignora o 2 e 3
