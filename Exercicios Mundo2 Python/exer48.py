s = 0
cont = 0
for c in range(1, 501):
    if c%3 == 0 and c%2 != 0:
        s += c
        cont = cont + 1
print("A Soma de todos {} impares que são multiplos de 3: {}".format(cont, s))
        
        