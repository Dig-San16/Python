salário = float(input("Digite seu salário: "))
if salário > 1250:
    aumento = 0.10
if salário < 1250:
    aumento = 0.15
soma = salário * aumento
print(f"Seu aumento será de: {soma}")
