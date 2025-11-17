#Operações lógicas podem ser combinadas em expressões lógicas mais complexas,
#utilizando-se de alguns operadores, veja a seguir:

              
                 #True or False and not True <-- a comparação começa aqui
                  #True or False and False
                      #True or False
                         #True


print(  True or False and not True   )




#olhe para esse comando...


salário = 100 
idade = 20 
salário2 = 2000 
idade2 = 30 

print(salário > 1000 and idade > 18) #1
print(salário2 > 1000 and idade2 > 18) #2

#Na primeira situação, o resultado será FALSO, pois:
#   "salario" < 1000 e "idade" > 18
#         FALSE    AND     TRUE


#Na segunda situação, o resultado será VERDADEIRO, pois:
#   "salario2" > 1000 e "idade2" > 18
#          TRUE     AND      TRUE
