# Programa que pede ao usuário para inserir seu nome, idade e altura, e imprime os valores com seus tipos.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (em metros): "))

print(f"Nome: {nome} (tipo: {type(nome)})")
print(f"Idade: {idade} (tipo: {type(idade)})")
print(f"Altura: {altura} (tipo: {type(altura)})")
