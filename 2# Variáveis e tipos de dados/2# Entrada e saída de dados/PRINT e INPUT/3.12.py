distancia = float(input("Qual foi a distância percorrida em km?: "))
velocidade = float(input("Qual foi a velocidade do carro em km/h?: "))
tempo_em_horas = distancia / velocidade
horas = int(tempo_em_horas)
minutos = int((tempo_em_horas - horas) * 60)
segundos = int(((tempo_em_horas - horas) * 60 - minutos) * 60)
print(f"O tempo estimado é {horas}:{minutos}:{segundos}")
