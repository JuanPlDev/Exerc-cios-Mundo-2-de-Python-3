s = 0
count = 0
while True:
    n = int(input('Digite um numero: [999 para parar]'))
    if n == 999:
        break
    count += 1
    s += n
print(f'A soma dos {count} valores foi {s}!')

