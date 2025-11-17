#A função OPEN é utilizada para abrir um arquivo em Python.

#WITH é usada em conjunto com OPEN para garantir que o arquivo
#seja fechado corretamente após a conclusão das operações.


with open(file='arquivo', mode='leitura', encoding='decodificador') as arquivo:
  bloco de código


#Acima, estão os respectivos parametros, na qual são responsáveis na forma de
#leitura do arquivo, são eles:

#FILE: armazena o arquivo

#MODE: descreve o tipo de leitura do arquivo

#ENCONDING: codifica os caracteres para interpretar o conteúdo do arquivo.
#(Muito útil para situações onde o texto está com caracteres acentuados,
#caracteres especiais ou caracteres de outros idiomas.)
