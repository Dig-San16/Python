salário = float(input("Digite o salário atual:"))
p_aumento = float(input("Digite a porcentagem de aumento:"))
aumento = salário * p_aumento / 100
novo_salário = salário + aumento
print(f"o aumento foi de {aumento}")
print(f"logo, novo salario é de {novo_salário}")
