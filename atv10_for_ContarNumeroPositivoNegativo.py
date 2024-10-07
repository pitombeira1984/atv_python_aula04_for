def ContarNumerosPositivoseNegativos():
  positivos = 0
  negativos = 0
  for numero in range(10):
    numero = int(input('Digite o numero: '))
    if numero > 0:
      positivos += 1
    elif numero < 0:
      negativos += 1
    print(f"Positivos: {positivos}")
    print(f"Negativos: {negativos}")
ContarNumerosPositivoseNegativos()
