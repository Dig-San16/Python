#O FATIAMENTO consiste em extrair partes de strings, no minimo, existe 2 tipos
#de fatiamento:

s = "ABCDE"

#Fatiamento fixo:

print(s[0]) #A

print(s[1]) #B

print(s[2]) #C

print(s[3]) #D


print(s[-1]) #E

print(s[-2]) #D

print(s[-3]) #C

print(s[-4]) #B
 

print("\n")

#Fatiamento por intervalo:

print(s[:])  #  ABCD

print(s[1:]) #  BCD

print(s[2:]) #  CD

print(s[3:]) #  D

print(s[:1]) #  A

print(s[:2]) #  AB

print(s[:3]) #  ABC

print(s[:4]) #  ABCD

print(s[:-1])#  ABC

print(s[:-2])#  AB

print(s[:-3])#  A

print(s[-1:])#  D

print(s[-2:])#  CD

print(s[-3:])#  BCD

print(s[-4:])#  ABCD

print(s[:2:3])# A

print("\n")

#vale ressaltar que a primeira string começa com o número 0

#       A   B   C   D   E
#       0   1   2   3   4

#o computador não irá imprimir "D" se vc escrever a exatamente a posição dele (que no caso seria 4).
#portanto, o número terá que ser 3 se quiser mostrar D.

print(s[3:4])
  