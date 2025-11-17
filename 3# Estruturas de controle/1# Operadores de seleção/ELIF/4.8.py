numero1 = int(input("escreva um numero: "))
numero2 = int(input("escreva outro numero: "))
calculo = input("escolha entre essas operações = +,-,x,/: ")
if calculo == "+":
    resultado = numero1 + numero2
elif calculo == "-":
    resultado = numero1 - numero2
elif calculo == "x":
    resultado = numero1 * numero2
elif calculo == "/":
    resultado = numero1 / numero2
else:
    print("nao foi possivel calcular isso ai n")
    
print(f"resultado é: {resultado}")

#ELIF é uma função utilizada para substituir o if aninhado(if dentro de um if).

#Extremamente util quando queremos mostrar mais de uma comparação.
