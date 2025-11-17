dia = int(input("quantos cigarros vc fuma por dia?: "))
ano = int(input("por quantos anos vc fumava?: "))
redução = 365 * ano * 60 * dia
vida = redução / (24 * 60)
print(f"vc perdera {vida} dias de vida")
