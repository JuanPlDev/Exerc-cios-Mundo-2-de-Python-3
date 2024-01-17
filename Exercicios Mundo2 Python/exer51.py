t = int(input("Digite o termo da progressão: "))
r = int(input('Digite a razão da progressão: '))
decimo = t + (10-1) * r
for c in range(t,decimo, r):        
    print("{}".format(c))
print("Acabou")
