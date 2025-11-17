#Heranças são usadas na intenção de reaproveitar código ou comportamento
#generalizado ou especializar operações ou atributos.

class NomeClasse(object):

  def __init__(self, params):
    ...

class NomeClasseEspecializada(NomeClasse):

  def __init__(self, params):
    super().__init__(self, params) #super() é uma função especial utilizada
    self.atributo3 = ...           #para acessar e chamar métodos da classe
    self.atributo4 = ...           #pai em uma hierarquia de
                                   #herança.
    
  def metodo3(self, params):
    ...

  def metodo4(self, params):
    ...
