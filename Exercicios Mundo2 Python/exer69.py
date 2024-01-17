countid = 0
countsx = 0
countm = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    i = int(input('Idade: '))
    if i > 18:
        countid += 1
    s = str(input('Sexo [M/F]')).upper()
    print('-'*20)
    while s != 'M' and s != 'F':
        s = str(input('Sexo [M/F]')).upper()
    if s == 'F' and i < 20:
        countm += 1
    if s == 'M':
        countsx += 1
    r = str(input('Quer continuar? [S/N]')).upper()
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar? [S/N]')).upper()
    if r == 'N':
        break
        
print('='*15, 'Fim do Programa', '='*15)
print(f'Total de pessoa com mais de 18 anos: {countid}')
print(f'Ao todo temos {countsx} homens cadastrados')
print(f'E temos {countm} mulheres com menos de 20 anos')


