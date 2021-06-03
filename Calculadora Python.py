import math
import cmath
import time
#Operaciones
def suma(n1+n2):
  return n1 + n2
def resta(n1,n2):
  return n1-n2
def division(n1,n2):
  try:
    resultado = n1/n2
    return resultado
  except ZeroDivisionError as e:
    print("ERROR ERROR Tu division es una division con un 0, porfavor espere 10 segundos y vuelva a ingresar sus números")
    time.sleep(10)
    info()
def multiplicacion(n1,n2):
  return n1*n2
def potencia(n1,n2):
  return n1**n2
def raiz(n1,n2):
  return n1**(1/x)
def raiz_cuadrada(n1,n2):
  return (sqrt(n1),sqrt(n2))
#Informacion del usuario
invalido_1 = False
def info():
  nombre = input('Bienvenido, ¿cuál es tu nombre?: ')
  print(str("Así que tu nombre es {0}, que fantastico nombre tienes").format(nombre))
  respuesta_1 = input("¿Quieres realizar una operación?(escribe en minusculas si o no): ")
if respuesta_1 == "si" and respuesta_3 != "si":
  arr[] = {"multiplicacion","suma","resta","division","potencias", "raíces", "raíz cuadrada"}
  print(str("Muy bien {0} necesito que me des el tipo de operacion que planeas realizar puedo hacer las siguientes operaciones: {1}").format(nombre, arr))
  respuesta_2 = int(input("Que escribe el numero del tipo de operación que planeas hacer(1-suma,2-resta,3-multiplicacion,4-division,5-potencia,6-raíces,7-raíz cuadrada): "))
  def esta(respuesta_2):
    if respuesta_2 > arr.lenght():
      return False
    else:
      return True
  esta(respuesta_2)
  if esta != True:
    print("La operación no esta dentro de las disponibles")
    time.sleep(10)
    invalido_1 = True
  else:
    n1 = int(input("Coloca tu primer numero: "))
    n2 = int(input("Coloca tu segundo numero(Si planeas realizar una raíz este número debe ser el grado de la raíz, numero2√numero1): "))
  if respuesta_2 == 1:
    result = suma(n1,n2)
    print(str("Sumamos los dos números: {0} y {1},realizamos la suma según la ley de signos, el resultado es {2}").format(n1,n2,result))
    return result
    time.sleep(10)
  elif respuesta_2 == 2:
    result = resta(n1,n2)
    print(str("Restamos los dos numeros formando la siguienta forma ({0})-({1}), realizamos la resta y su resultado será {2}").format(n1,n2,result))
    return result
  elif respuesta_2 == 3:
    result = multiplicacion(n1,n2)
    return result
  elif respuesta_2 == 4:
    result = division(n1,n2)
    return result
  elif respuesta_2 == 5:
    result = potencia(n1,n2)
    return result
  elif respuesta_2 == 6:
    result = raiz(n1,n2)
    return result
  elif respuesta_2 == 7:
    result = raiz_cuadrada(n1,n2)
    return result
  else:
    invalido_1 = True
  print("Ufff, esos calculos me han dado un dolor de cabeza, ¿porque no aprovechas a copiar el resultado?")
  return result
  time.sleep(4)
  save = input("Bueno supongo que ya lo copiaste o ¿quieres que lo guarde por ti?(si o no): ")
  if save == "si":
    n3 = result
  else:
    n3 = 0
  acciones[] = {"1.Hacer otra operacion","2.Recordarte el resultado", "3.Hacer otra operacion con el resultado anterior","4. Leerte un cuento","5. Adios"}
  
  for i in acciones:
    print
elif respuesta_1 == "no":
  print(str("Entendido usuario todo poderoso cuyo nombre es {0}").format(nombre))
  print("Espero que tenga un buen día")
  x = 10
  time.sleep(x)
  break
else:
  invalido_1 = True
while invalido_1:
  info()
