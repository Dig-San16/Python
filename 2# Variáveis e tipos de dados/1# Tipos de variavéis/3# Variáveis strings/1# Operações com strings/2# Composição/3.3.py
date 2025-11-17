#existe 3 métodos de marcar posições, veja:

nome = "joão"
idade = 22
grana = 5560

#F-strings

print(f"{nome} tem {idade} anos e R${grana:.2f} de grana.")

#Format

print("{} tem {} anos e R${:.2f} de grana." .format(nome, idade, grana))

#Método clássico

print("%s tem %d anos e R$%.2f de grana." % (nome, idade, grana))


#o método clássico é o mais portável entre várias linguagens, porém, 
#quando o assunto é python, f-strings é a melhor opção.
