import random

print('Vamos Jogar Par ou Impar')
count = 0
while True:
    print('='*25)
    c = random. randint(0, 10)
    v = int(input('Digite um valor: '))
    poui = str(input('Par ou Impar? ')).upper()
    s = c+v
    if s%2 == 0 and poui == 'PAR':
        print('='*25)
        print(f'Você jogou {v} e o computador {c}. Total de {s} deu PAR')
        print('='*25)
        count += 1
        print('Você Venceu !')
        print('Vamos Jogar novamente...')
    if s%2 != 0 and poui == 'IMPAR':
        print('='*25)
        print(f'Você jogou {v} e o computador {c}. Total de {s} deu IMPAR')
        print('='*25)
        count += 1
        print('Você Venceu !')
        print('Vamos Jogar novamente...')
    elif s%2 != 0 and poui != 'IMPAR':
        print('='*25)
        print(f'Você jogou {v} e o computador {c}. Total de {s} deu Impar')
        print('='*25)
        print('Você Perdeu !')
        print('='*25)
        print(f'GAME OVER. Você venceu {count}')
        break
    else:
         print('='*25)
         print(f'Você jogou {v} e o computador {c}. Total de {s} deu PAR')
         print('='*25)
         print('Você Perdeu !')
         print('='*25)
         print(f'GAME OVER. Você venceu {count}')
         break
    


