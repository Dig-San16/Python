#Com a manipulação, podemos separar alguns dos demais formatos de código
#que estão abaixo.

#ATRIBUTOS: Características da classe, ou seja, são as informações que cada
#           objeto terá

class Pessoa():
    def __init__(self, nome: str, idade: int): 
        self.nome = nome 
        self.idade = idade
        
#MÈTODOS: Ações que os objetos da classe podem realizar

    def maior_de_idade(self):
        return self.idade >= 18
    
    def dormir(self, horas: int):
        print(f"{self.nome} está dormindo por {horas} horas.")

    def falar(self, texto=str):
        print(texto)

#OBJETOS: Instancia da classe 

Ramon = Pessoa(nome='Ramon Dino', idade=30)


Ramon.dormir(horas=8)


if Ramon.maior_de_idade():
    print(f'{Ramon.nome} é maior de idade')
else:
    print(f'{Ramon.nome} não é maior de idade')
    

Ramon.falar("Se quiser sim mano")
