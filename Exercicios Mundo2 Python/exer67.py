
while True:
    n = int(input("Quer ver a tabuada de qual valor? "))
    if n < 1:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break
    for count in range(0,11):
        print(f'{n} x {count} = {n * count}')