s = 0
count = 0
menor = 99999
while True:
    print('='*20)
    print('Loja de 1 Real')
    print('='*20)
    nomep = str(input('Nome do produto: '))
    precop = float(input('Preço: R$'))
    if precop < menor:
        menor = precop
        nome = nomep
    s += precop
    r = str(input('Quer continuar [S/N] ')).upper()
    while r != 'S' and r != 'N':
        r = str(input('Quer continuar [S/N] ')).upper()
    if precop > 1000:
        count += 1
    if r == 'N':
        break
print('='*15, 'Fim do Programa', '='*15)
print(f'O total de compras foi {s}')
print(f'Temos {count} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome} que custa R${menor}')

