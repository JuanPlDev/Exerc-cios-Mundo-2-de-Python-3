count = 1
s = 0
while count < 999:
    n = int(input('Digite digite um numero: [999 para parar]'))
    if n != 999:
        s = s + n
        count += 1
    if n == 999:
        break
    
print('Foram digitados {} numero, e a soma entre eles foi {}'.format(count-1,s))