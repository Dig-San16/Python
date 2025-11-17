salario = float(input("qual seu salario?: "))
if salario > 1250: 
    aumento = 0.10
else: 
    aumento = 0.15
soma = salario * aumento
print(f"o aumento foi de: R$%.2f" % soma)
 
#ELSE é uma função responsável por avaliar uma condição OPOSTA,
#sendo ela VERDADEIRA ou FALSA.


