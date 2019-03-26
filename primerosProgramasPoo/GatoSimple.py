'''
Vamos a crear la clase GatoSimple. La llamamos así porque más adelante crearemos otra
clase algo más elaborada que se llamará Gato. Para saber qué atributos debe tener esta
clase hay que preguntarse qué características tienen los gatos. Todos los gatos son de
un color determinado, pertenecen a una raza, tienen una edad, tienen un determinado
sexo - son machos o hembras - y tienen un peso que se puede expresar en kilogramos.
Éstos serán por tanto los atributos que tendrá la clase GatoSimple.
Para saber qué metodos debemos implementar hay que preguntarse qué acciones
están asociadas a los gatos. Bien, pues los gatos maullan, ronronean, comen y si son
machos se pelean entre ellos para disputarse el favor de las hembras. Esos serán los
métodos que definamos en la clase.

@author: Rafael Infante
'''
class GatoSimple: #clase gato simple
  
  def __init__(self,s): #constructor
    self.sexo=s
    self.color=""
    self.raza=""
    self.edad=0
    self.peso=0
    
  #getter
  def obtenersexo(self):
    return self.sexo
  
  '''
  metodo que hace que el gato maulle
  
  '''
  def maulla(self):
    print("Miauuu")
    
  '''
  metodo que hace que el gato ronronee
  
  '''
  def ronronea(self):
    print("mrrrrr")
  
  '''
  metodo que hace que el gato coma.
  A los gatos les gusta el pescado, si le damos otra comida
  la rechazará.
  
  '''  
  def come(self,comida):
    if comida=="pescado":
      print("hmmm gracias")
    else:
      print("Lo siento, yo solo como pescado")
  
  '''
  metodo que hace que se pellen los gatos
  '''
  def peleaCon(self,contrincante):
    if (self.sexo=="hembra"):
      print("no me gusta pelear")
    else:
      if (contrincante.obtenersexo()=="hembra"):
        print("no peleo contra gatitas");
      else:
        print("ven aqui que te vas a enterar");
        
      
'''
garfield = GatoSimple("macho")
tom = GatoSimple("macho")
lisa = GatoSimple("hembra")
maria = GatoSimple("hembra")
lisa.peleaCon(maria)
'''
  