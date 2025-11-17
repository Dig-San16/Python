distancia = int(input("qual a distancia que deseja percorrer em km?: "))
if distancia > 200:
    real = 0.45
else:
    real = 0.50
soma = distancia * real
print(f"vc pagará {soma} reais pelo preço da passagem")
