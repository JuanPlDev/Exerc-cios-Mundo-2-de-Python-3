n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''-------Menu---------
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
            print('A soma dos valores é {}'.format(n1+n2))
    elif opcao == 2:
            print('A multiplicação dos valoeres é {}'.format(n1*n2))
    elif opcao == 3:
           if n1 > n2:
                  maior = n1
           else:
                  maior = n2 
           print('Entre {} e {} o maior valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
           print('Informe os numeros novamente: ')
           n1 = int(input('Digite o primeiro valor: '))
           n2 = int(input('Digite o segundo valor: '))

    elif opcao == 5:
           print('Finalizando')
    else: 
        print('opção invalida. Tente novamente')
print('Promagrama finalizado')


        


    
    