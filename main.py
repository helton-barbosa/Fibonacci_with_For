number = int(input('Entre com a quantidade de termos: '))
a = 0
b = 1

for contador in range(number):
    print(f'Termo de número [{contador+1}]: {a}')
    c = a + b
    a = b
    b = c
