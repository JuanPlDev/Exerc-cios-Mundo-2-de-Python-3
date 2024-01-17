s = 0
count = 0
for c in range(0,6):
    n = int(input('Digite um numero? '))
    if n%2 == 0:
        s += n
        count = count + 1
print("A soma dos {} pares é {}".format(count,s))
