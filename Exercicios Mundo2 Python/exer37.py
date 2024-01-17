n = int(input('Digite um número inteiro: '))
print(''' Escolha uma base para conversão:
[1] Converter para Binário
[2] Converter para Octal 
[3] Converter para Hexadecimal''')
opcao = int(input("Sua opção: "))
if opcao == 1:
    print("O valor de {} convertido para Binário é {}".format(n, bin(n)[2:]))
elif opcao == 2:
    print("O valor de {} convertido para Octal é {}".format(n, oct(n) [2:]))
elif opcao == 3:
    print("O valor de {} convertido para Hexadecimal é {}".format(n, hex(n)[2:] ))
else:
    print("Opção invalida")
