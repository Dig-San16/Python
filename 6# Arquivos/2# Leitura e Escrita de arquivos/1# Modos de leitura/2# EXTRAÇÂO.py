#A EXTRAÇÂO consiste em extrair valores do arquivo. 

def extrai_coluna(nome_arquivo: str, indice_coluna: int, tipo_dado: str):

  coluna = []

  with open(nome_arquivo, 'r', encoding='utf8') as na:
      line = na.readline() #le o cabeçalho
      line = na.readline() #le a primeira linha
      while line:
          lineSep = line.split(',') #separa os valores por virgula e salva isso
                                    #em uma lista
          indice = lineSep[indice_coluna] #indice vira uma lista
          if tipo_dado == 'str':
            str(indice)
          elif tipo_dado == 'int':
            int(indice)
          else:
            float(indice)
          coluna.append(indice) 
          line = na.readline()

  return coluna

valor_venda = extrai_coluna(nome_arquivo='carros.py', indice_coluna=2, tipo_dado='str')
print(valor_venda)
