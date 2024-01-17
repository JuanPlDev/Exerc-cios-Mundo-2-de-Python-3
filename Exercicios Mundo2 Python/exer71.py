print('='*35)
print(' '*10,'BANCO JFPS')
print('='*35)
vs = int(input('Qual valor você quer sacar? R$'))
c50 = vs//50
resto = vs - c50 * 50 
c20 = resto // 20
resto1 = resto%20
c10 = resto1//10
resto2 = resto1%10
c1 = resto2//1
if c50 != 0:
    print(f'Total de {c50} cédulas de R$50')
if c20 != 0:
    print(f'Total de {c20} cédulas de R$20')
if c10 != 0:
    print(f'Total de {c10} cédulas de R$10')
if c1 != 0:
    print(f'Total de {c1} cédulas de R$1')
print('='*20)
print('Volte sempre ao BANCO JFPS! Tenha um Bom dia')
