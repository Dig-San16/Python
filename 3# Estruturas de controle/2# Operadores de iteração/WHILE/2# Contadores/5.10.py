pontos = 0
questão = 1
while questão <= 3:
    resposta = input(f"resposta da questão {questão}: ") #1
    if questão == 1 and (resposta == "b" or resposta == "B"): #2
        pontos = pontos + 1
    if questão == 2 and (resposta == "a" or resposta == "A"): #3
        pontos = pontos + 1
    if questão == 3 and (resposta == "d" or resposta == "D"): #4
        pontos = pontos + 1  
    questão = questão + 1
print(f"O aluno fez {pontos} ponto(s)")

#vamos entender esse programa:

#em 1, a estrutura irá repetir a frase = ("resposta da questão {questão}: "),
#quando for digitado um valor na variavel "resposta"

#em 2,3 e 4, estão as condições com os seus respectivos operadores lógicos
#AND e OR.

#imagine o segunite:

#sabemos que a variavel "questão" é verdadeira, pois receberá 1 a cada
#digito.

#se na variavel "resposta" for digitado os B´s maiusculo ou minusculo,
#será executado o contador "pontos", ou seja, pontos recebera 1 por ter digitado
#a resposta correta.

#caso for o contrario, como, ter digitado uma letra ou numero aleatorio não
#correspondente, a resposta será falsa e a variavel "pontos" não será executada.
    
#execute o programa, digite valores, e o compare com essa ideia abaixo:

# TRUE AND TRUE OR FALSE / TRUE AND FALSE OR TRUE / TRUE AND FALSE OR FALSE
#     TRUE AND TRUE            TRUE AND TRUE            TRUE AND FALSE           
#          TRUE                     TRUE                    FALSE            
