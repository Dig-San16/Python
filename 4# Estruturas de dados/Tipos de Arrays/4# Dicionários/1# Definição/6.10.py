#Podemos criar dicionários compostos:

cadastro = {
    "Tony": {
        "nome": "Tony Stark", #1
        "ano_nascimento": "???", #2
        "pais": {
            "pai": {
                "nome": "???", #3
                "ano_nascimento": "1917", #4
            },
            "mãe": {
                "nome": "Maria Stark", #5
                "ano_nascimento": "1919", #6
            }
        }
    }
}

#Nas seis linhas, deve-se terminar com virgula para evitar erros.

cadastro["Tony"]["ano_nascimento"] = ["1970"]
cadastro["Tony"]["pais"]["pai"]["nome"] = ["Howard Stark"]

print(cadastro)

#Os valores em um dicionário só podem ser atualizados ou acessados por meio de suas respectivas chaves.

