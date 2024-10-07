def NumerosParesImpares():
  for numero in  range(1, 20):
    if  numero % 2 == 0:
      print(f"O número {numero} é par")
    else:
      print(f"O número {numero} é impar")
    if  numero == 15:
      print(f"O número {numero} é especial paramos por aqui")
      break 
NumerosParesImpares()
