deposito = int(input("qual o depósito inicial?: "))
taxa = float(input("qual a taxa de juros?: "))

mes = 1
while mes <= 24:
     deposito = deposito + (deposito * (taxa / 100))
     print(f"total ganho no {mes} mes: {deposito:.2f}")
     mes = mes + 1
print(f"O total ganho com juros nos periódos é {deposito:.2f}")
