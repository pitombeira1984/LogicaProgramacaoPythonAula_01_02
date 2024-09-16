idade1 = int(input("Digite sua idade: "))
idade2 = int(input("Digite sua idade: "))

if idade1 == idade2:
    print('Idades iguais')
elif idade1 > idade2:
    print(f'{idade1} é maior que {idade2}')
else:
    print(f'{idade2} é maior que {idade1}')