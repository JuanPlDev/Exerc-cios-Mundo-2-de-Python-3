import time
from random import choice
lista = ['pedra', 'papel', 'tesoura']
com = choice(lista)
usu = int(input('''VAMOS JOGAR JOKENPÔ
(1) Para você escolher pedra
(2) Para você escolher papel
(3) Para você escolher tesoura 
'''))
print("Pensei na minha jogada vamos lá")
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PÔ")
if usu == 1:
    usu = 'pedra'
elif usu == 2:
    usu = 'papel'
elif usu == 3:
    usu = 'tesoura'


print("Computador: {}    Usuario: {}".format(com, usu))
if usu == 'pedra' and com == 'pedra' or usu == 'tesoura' and com == 'tesoura' or usu == 'papel' and com == 'papel':
    print("XIIIIIIII DEU EMPETA BORA JOGAR DENOVO")
elif usu == 'papel' and com == 'tesoura' or usu == "tesoura" and com == "pedra" or usu == 'pedra' and com == 'papel':
    print('HAHA EU GANHEI ')
elif usu == 'tesoura' and com == 'papel' or usu == 'pedra' and com == 'tesoura' or usu == 'papel' and com == 'pedra':
    print("HAHA PARABÉNS VOCÊ GANHOU")

    




