class Pessoa:

#Atributos da Classe Pai (Pessoa)
    
    def __init__(self, nome: str, idade: int, documento: str):
        self.nome = nome
        self.idade = idade
        self.documento = documento
        
    def __str__(self) -> str: #O método especial __str__ é usado para fornecer
                              #uma representação em string personalizada para a
                              #instância da classe. Retorna uma string formatada
                              #contendo o nome, idade e número do documento.
        
        return f'{self.nome}, {self.idade} anos e documento número {self.documento}'

#Classe Estudante: Herdeira da classe Pessoa

class Estudante(Pessoa):

    def __init__(self, nome: str, idade: int, documento: str):
        super().__init__(nome=nome, idade=idade, documento=documento)

andre = Estudante(nome='Andre Perez', idade=30, documento='123')

print(andre)
