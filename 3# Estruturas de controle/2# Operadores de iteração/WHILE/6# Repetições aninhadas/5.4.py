#Repetições aninhadas refere-se a combinação de vários "whiles" de forma
#a obter novos resultados

tabuada = 1
while tabuada <= 10:#1
    número = 1 #2
    while número <= 10: #3
        print(f"{tabuada} x {número} = {tabuada * número}")
        número += 1 #4
    tabuada += 1 #5

#Na primeira linha, temos o primeiro WHILE, que irá repetir o quinto bloco
#enquanto o valor da tabuada for menor ou igual a 10

#Na segunda linha, inicializa outra variável dentro do primeiro WHILE. Possui
#muita importancia para multiplicar por 1 a cada novo valor da variável "tabuada"

#Na terceira linha, temos o segundo WHILE que, assim como o primeiro,
#irá repetir o quarto bloco enquanto o valor da tabuada for menor ou igual a 10
