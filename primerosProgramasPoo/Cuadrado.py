'''
Clase Cuadrado y prueba del metodo toString en python3

@author: Rafael Infante
'''
class Cuadrado:
  
  #constructor
  def __init__(self,l):
    self.lado=l
  
  #metodo toString
  def __str__(self):
    resultado=""
    for i in range(0,self.lado):
      resultado+="[]"
    resultado+="\n"
    
    for i in range(1,(self.lado-1)):
      resultado+="[]"
      for espacios in range(1,(self.lado-1)):
        resultado+="  "
      resultado+="[]\n"
    
    for i in range(0,self.lado):
      resultado+="[]"
    resultado += "\n"
    return resultado