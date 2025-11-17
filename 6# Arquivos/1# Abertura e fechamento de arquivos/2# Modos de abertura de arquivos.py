#Os modos de abertura são representados por uma string que é passada como
#argumento para a função OPEN. Aqui estão alguns modos comuns:

#'R'(read): Modo padrão. Abre o arquivo para leitura. Se o arquivo não existir,
#gera um erro.

with open('exemplo.txt', 'r') as arquivo:
    

#'W'(write): Abre o arquivo para escrita. Se o arquivo existir,
#ele é truncado (todo o conteúdo é apagado). Se o arquivo não existir,
#cria um novo.

with open('exemplo.txt', 'w') as arquivo:


#'A' (append): Abre o arquivo para escrita. Se o arquivo existir, o conteúdo
#é mantido e novos dados são adicionados ao final. Se o arquivo não existir,
#cria um novo.

with open('exemplo.txt', 'a') as arquivo:


#'B' (binary): Modificador que pode ser adicionado a outros modos para tratar
#o arquivo como binário. Exemplo: 'rb', 'wb', 'ab'

with open('imagem.png', 'rb') as arquivo_binario:


#'x' (exclusive creation): Cria um novo arquivo e o abre para escrita.
#Se o arquivo já existir, gera um erro.


with open('novo_arquivo.txt', 'x') as novo_arquivo:
