deposito = float(input("qual o depósito inicial?: "))
taxa = float(input("qual a taxa de juros?: "))
depomensal = float(input("qual o valor depositado mensalmente?: "))

mes = 1
while mes <= 24:
     deposito = deposito + (deposito * (taxa / 100) + depomensal)
     print(f"total ganho no {mes} mes: {deposito:5.2f}")
     mes = mes + 1
print(f"O total ganho com juros nos periódos é {deposito:10.2f}")
