import random
num = random.randint(0,10)
n = int(input('''Sou seu computador... 
Acabei de pensar em numero de 0 a 10.
Será que você consegue advinhar qual foi?
Qual é o seu palpite: '''))
a = 0
while n != num:
    a = a + 1
    if n < num:
        n = int(input('Mais... Tente mais uma vez. '))
    if n > num:
        n = int(input('Menos... Tente mais uma vez. '))
    if n == num:
        break
print('Parabéns você acertou o numero que eu pensei foi {}, e foram necessario {} palpites para o acerto'.format(num, a))