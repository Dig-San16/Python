dias = int(input("quantos Dias?:"))
horas = int(input("quantas Horas?:"))
minutos = int(input("quantos Minutos?:"))
segundos = int(input("quants Segundos?:"))
total_em_segundos = dias * 24 * 3600 + horas * 3600 + minutos * 60 + segundos
print(f"Convertido em segundos é igual a {total_em_segundos} segundos.")
