a = int(input("numero: "))
b = int(input("numero: "))
c = int(input("numero: "))
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c
print(f"o maior numero é {maior}")
print(f"o menor numero é {menor}")
