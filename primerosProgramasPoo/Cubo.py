'''Vamos a crear la clase Cubo. Para saber qué atributos se deben definir, nos preguntamos
qué características tienen los cubos - igual que hicimos con la clase GatoSimple. Todos los
cubos tienen una determinada capacidad, un color, están hechos de un determinado
material - plástico, latón, etc. - y puede que tengan asa o puede que no. Un cubo se
fabrica con el propósito de contener líquido; por tanto otra característica es la cantidad
de litros de líquido que contiene en un momento determinado. Por ahora, solo nos
interesa saber la capacidad máxima y los litros que contiene el cubo en cada momento,
así que esos serán los atributos que tendremos en cuenta.

@author: Rafael Infante'''

class Cubo:

  # constructor
  def __init__(self, c):
    self.capacidad = c
    self.contenido = 0

  # metodos getter
  def getCapacidad(self):
    return self.capacidad

  def getContenido(self):
    return self.contenido
  
  #metodos setter
  def setContenido(self,litros):
    self.contenido=litros
  
  #otros metodos
  
  def vacia(self):
    self.contenido=0
  
  #llena el cubo al maximo
  def llena(self):
    self.contenido=self.capacidad
  
  '''Pinta el cubo en la pantalla.
  Se muestran los bordes del cubo con el carácter # y el
  agua que contiene con el carácter ~.
  '''
  def pinta(self):
    nivel=self.capacidad
    for nivel in range(nivel,0,-1):
      if self.contenido>=nivel:
        print("#~~~~#")
      else:
        print("#    #")
    print("######")
  
  '''Vuelca el contenido de un cubo sobre otro.
  Antes de echar el agua se comprueba cuánto le cabe al
  cubo destino.'''
  def vuelcaEn(self, destino):
    #obtengo el contenido del cubo destino
    libres=destino.getCapacidad()- destino.getContenido()
    if libres>0:
      if self.contenido<=libres:
    #pongo el contenido de los dos cubos en el de destino
        destino.setContenido(destino.getContenido()+self.contenido)
        self.vacia()
      else:
        self.contenido-=libres
        destino.llena()
  
      
'''miCubo=Cubo(4)
print(miCubo.pinta())'''
 
