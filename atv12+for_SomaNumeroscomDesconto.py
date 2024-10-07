def SomaNumeroscomDesconto():
    soma = 0
    pcfinal = 0

    for _ in range(5):
        produto = float(input('Digite o preço do produto: '))
        soma += produto
        if soma >= 100:
            break
        
    if soma >= 100:
        pcfinal = soma - (soma * 0.1)
    else:
        pcfinal = soma

    print(f'O valor total é {pcfinal:.2f}')
SomaNumeroscomDesconto()