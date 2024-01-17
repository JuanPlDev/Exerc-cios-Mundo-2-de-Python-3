count = 0
maior = 0
menor = 9999
s = 0
while count != 'n':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    s = s + n
    count += 1
    r = str(input("Quer continua [S/N] ")).upper()
    if r != 'S':
        break
print("Você digitou {} números e média entre os valores foram {:.2f}\nO maior foi {} e o menor foi {} ".format(count,s/count, maior, menor))