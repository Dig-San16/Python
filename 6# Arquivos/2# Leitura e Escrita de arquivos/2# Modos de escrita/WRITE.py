#Write é uma função de escrita para arquivos, ela apaga o arquivo
#original para reescreve-lo:

with open ('impares.txt','w') as impares, open('pares.txt', 'w') as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f'{n}')#1
        else:
            impares.write(f'{n}')#2

#'W' abre o arquivo para escrita, sobreescreve o arquivo original ou cria um
#novo arquivo.

with open ('impares.txt','a') as impares, open('pares.txt', 'a') as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f'{n}\n')#3
        else:
            impares.write(f'{n}\n')#4

#'A' abre o arquivo para escrita, não sobreescreve, mas acrescenta
#coisas no arquivo original.
            
#O WRITE é utilizado para executar os dois arquivos e é considerado um método nativo,
#especialmente criado para mostrar como será escrito um arquivo. 
