KWH = int(input("qual a quantidade de kWh consumida?:"))
instalação = input("qual o tipo de instalação? residencial,comercial ou industrial?:")
if instalação == "residencial":
    if KWH <= 500:
        preço = 0.40
    else:
        preço = 0.65
elif instalação == "comercial":
    if KWH <= 1000:
        preço = 0.55
    else:
        preço = 0.60
elif instalação == "indsutrial":
    if KWH <= 5000:
        preço = 0.55
    else:
        preço = 0.60
else:
    preço = 0
    print("Erro ! Tipo de instalação desconhecido!")
    
custo = KWH * preço   
print(f"tu pagarará {custo:.2f}")


