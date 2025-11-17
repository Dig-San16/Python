preço = float(input("Digite o preço da mercadoria:"))
desconto = float(input("Digite o percentual de desconto:"))
valor_do_desconto = preço * desconto / 100
pagar = preço - valor_do_desconto
print(f"o valor do desconto é {valor_do_desconto}")
print(f"logo, o preço a pagar é {pagar}")
