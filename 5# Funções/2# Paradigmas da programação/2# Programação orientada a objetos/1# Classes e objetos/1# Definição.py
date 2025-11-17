# Classes são estruturas fundamentais na programação orientada a objetos (POO),
# ela serve como um modelo ou uma estrutura que define características e
# comportamentos comuns a um conjunto de objetos.

# Uma classe encapsula dados (ATRIBUTOS) que são as características da classe,
# e comportamentos (MÉTODOS) que estão relacionados às ações da classe.

class NomeClasse:
    # "self" é uma convenção usada para
    # representar o próprio objeto
    # instanciado a partir dessa classe

    def __init__(self, atributo1, atributo2):
        # "__init__" é um método especial utilizado para
        # inicializar os atributos da classe.
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def método1(self, param):
        # Exemplo de método que utiliza um parâmetro
        print(f"Executando método1 com o parâmetro: {param}")

    def método2(self, param):
        # Exemplo de método que utiliza um parâmetro e os atributos da classe
        print(f"Executando método2 com o parâmetro: {param}")
        print(f"Atributo1: {self.atributo1}, Atributo2: {self.atributo2}")

# Objetos são instâncias de uma classe, e servem para modelar e
# representar entidades do mundo real, conceitos ou abstrações no código
# de maneira mais organizada e estruturada.

# Criando um objeto da classe NomeClasse com valores para os atributos
objeto = NomeClasse("valor1", "valor2")

# Chamando métodos do objeto criado
objeto.método1("param1")
objeto.método2("param2")
