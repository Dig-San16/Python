#O arquivo "entrada" (na qual está dentro da pasta Pacotes) 
#contém uma função chamada válida_inteiro que solicita ao
#usuário a entrada de um número inteiro dentro de um intervalo
#especificado.

from Pacotes import entrada #importamos o arquivo

l = []
for x in range(10): #Em seguida, o código principal usa essa função para
                    #coletar 10 números inteiros
    
    l.append(entrada.válida_inteiro("digite um número: ", 0, 10)) #isso tudo em um intervalo de 0 a 10,
                                                                  #e então calcula a soma desses números.
print(f"Soma: {sum(l)}")
