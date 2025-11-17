def válida_inteiro(mensagem, mínimo, máximo):
    while True:
        try:
            v = int(input(mensagem))
            if v >= mínimo and v <= máximo:
                return v
            else:
                print(f'digite um valor entre {mínimo} e {máximo}')
        except ValueError:
            print("voce deve digitar um número inteiro")
             
