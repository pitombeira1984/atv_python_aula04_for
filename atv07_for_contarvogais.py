def contarvogais():
    texto = input("Digite uma frase: ")
    contador_vogais = 0
    for caractere in texto:
        if caractere.lower() in "aeiou":
            contador_vogais += 1
    print(f"Número de Vogais: {contador_vogais}")

contarvogais()