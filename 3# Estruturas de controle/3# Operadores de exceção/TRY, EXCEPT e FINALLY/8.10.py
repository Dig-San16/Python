#O TRY e EXCEPT são blocos utilizados para
#lidar com exceções durante a execução do programa:

while True:
    try: 
        # Código que pode gerar uma exceção
        numero = int(input("Digite um número para dividir por 10: "))
        resultado = 10 / numero
        print("Resultado:", resultado)

    except ValueError:
        # Código a ser executado se uma exceção do tipo ValueError ocorrer
        print("digite um número válido!")

    except ZeroDivisionError:
        # Código a ser executado se uma exceção do tipo ZeroDivisionError ocorrer
        print("Não é possível dividir por zero.")

    except Exception as e:
        #EXCPETION captura qualquer outra exceção não tratada pelos blocos
        #anteriores, AS apenas nomeia o erro.
        print(f"Ocorreu uma exceção: {e}")

    finally:
        # Bloco opcional que é sempre executado, independentemente de ocorrer
        #um erro ou não
        print("Eu sou sempre executado...")
    

