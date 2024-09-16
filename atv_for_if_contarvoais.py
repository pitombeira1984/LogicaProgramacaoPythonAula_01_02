def contar_vogais(palavra):
    vogais = 'aeiouAEIOU'
    total_vogais = 0

    for letra in palavra:
        if letra in vogais:
            total_vogais += 1
    
    return total_vogais

# Exemplo de uso
palavra = input("Digite uma palavra: ")
print(f"O número de vogais em '{palavra}' é: {contar_vogais(palavra)}")

