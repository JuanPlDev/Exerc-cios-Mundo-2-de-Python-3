c1 = int(input("Digite o primeiro comprimento: "))
c2 = int(input("Digite o segundo comprimento: "))
c3 = int(input("Digite o terceiro comprimento: "))
if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
    print("Pode formar um triângulo")
else:
    print("Não pode forma um triângulo")
if c1 == c2 and c1 == c3:
    print("Esse é um triângulo equilatero")
elif c1 == c2 != c3 or c1 == c3 != c2:
    print('Esse é um triângulo isósceles')
elif c1 != c2 or c1 != c3 or c2 != c3:
    print('Esse é um triângulo escaleno')