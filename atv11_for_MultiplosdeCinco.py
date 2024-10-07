def MultiplosdeCinco():
  for numero in range(1,31):
    if numero % 5 == 0:
      print(f"{numero} é divisível por 5")
      if numero > 20:
        print(f"Número {numero} é o primeiro divisível por 5 maior que 20")
        break
MultiplosdeCinco()
