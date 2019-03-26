'''
Crea una clase Fraccion (en Java yPython) de forma que podamos hacer las siguientes operaciones:

  Contruir un objeto Fraccion pasándole al constructor el numerador y el denominador.
  Obtener la fracción.
  Obtener y modificar numerador y denominador. No se puede dividir por cero.
  Obtener resultado de la fracción (número real).
  Multiplicar la fracción por un número.
  Multiplicar, sumar y restar fracciones.
  Simplificar la fracción.

@version:1.0
@author: Rafael Infante

'''

class Fraccion:
  
  '''
  constructor le pasamos como argumentos numerador y denominador
  
  @param: numerador
  @param: denominador
  '''
  def __init__(self,numerador,denominador):
    self.numerador=numerador
    self.denominador=denominador
    
  '''
  funcion para obtener la fraccion.
   
  @return: String
  '''
  def obtenerFraccion(self):
    return str(self.numerador) + "/" + str(self.denominador)
  
  '''
  funcion que modifica el numerador y denominador de la fraccion.
    
  @param: numerador
  @param: denominador
  '''
  def modificaFraccion(self,numerador,denominador):
    if denominador==0:
      print("No se puede dividir el denominador es igual a 0.")
    else:
      self.numerador=numerador
      self.denominador=denominador
  
  '''
  metodo que en el que obtienes el resultado de dividir numerador y 
  denominador de la fraccion.
   
  @return: un numero entero
  '''
  def resultadoFraccion(self):
    return self.numerador/self.denominador
  
  '''
  metodo que multiplica la fraccion por un numero.
  
  @param: un numero entero
  '''
  def multiplicaFraccionPorUnNumero(self,numero):
    self.numerador*=numero
 
  '''
  metodo que resta fracciones.
  
  @param: int numerador
  @param: int denominador
  '''
  def restarFracciones(self,numerador,denominador):
    if self.denominador == denominador:
      self.numerador-=numerador
    else:
      #multiplicamos los denominadores
      var3=self.denominador*denominador
      #calculamos el resultado del primer numerador
      var1=var3/self.denominador
      var1*=self.numerador
      #calculamos el resultado del segundo numerador
      var2=var3/denominador
      var2*=numerador
      #restamos los numeradores
      self.numerador=int(var1-var2)
      self.denominador=var3
    
  '''
  metodo que suma fracciones.
  
  @param: int numerador
  @param: int denominador
  '''
  def sumarFracciones(self,numerador,denominador):
    if self.denominador == denominador:
      self.numerador-=numerador
    else:
      #multiplicamos los denominadores
      var3=self.denominador*denominador
      #calculamos el resultado del primer numerador
      var1=var3/self.denominador
      var1*=self.numerador
      #calculamos el resultado del segundo numerador
      var2=var3/denominador
      var2*=numerador
      #restamos los numeradores
      self.numerador=int(var1+var2)
      self.denominador=var3
    
  '''
  metodo que multiplica fracciones.
  
  @param: int numerador
  @param: int denominador
  '''
  def multiplicaFracciones(self,numerador,denominador):
    self.numerador *= numerador
    self.denominador*=denominador
  
  '''
  halla el M.C.D de los denominadores de las fracciones
  '''
  def hallarMcd(self):
    dividendo=self.numerador
    divisor=self.denominador
    while dividendo%divisor!=0:
      resto = dividendo%divisor
      dividendo=divisor
      divisor=resto
    return divisor
  
  '''
  Funcion que simplifica fracciones al maximo
  '''
  def simplificarFraccion(self):
    mcd=self.hallarMcd()
    self.numerador=self.numerador//mcd
    self.denominador=self.denominador//mcd
  