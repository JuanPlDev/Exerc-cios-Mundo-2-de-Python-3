maior = 0
menor = 9999
for c in range(1,6):
    p = float(input('Digite o seu peso: '))
    if p > maior:
        maior = p
    elif p < menor:
        menor = p
print('O maior peso é {:.2f} e o menor peso é {:.2f}'.format(maior,menor))