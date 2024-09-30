def SomarNumerosPares():
    soma_numeros_pares = 0
    
    for numero in range(1, 51):
    
        if numero % 2 == 0:
            soma_numeros_pares += numero  


    print(f"Soma dos Números Pares: {soma_numeros_pares}")
    
SomarNumerosPares()
