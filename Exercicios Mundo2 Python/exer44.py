v = float(input("Digite o valor do produto: "))
o = int(input('''
Opções de pagamento:
(1) à vista dinheiro/cheque: 10% de desconto
(2) à vista no cartão: 5% de desconto
(3) em até 2x no cartão: preço normal
(4) 3x ou mais no cartão: 20% de juros
\nDigite a opção de pagamento:'''))
if o == 1:
    print("O valor do produto fica R${:.2f}".format(v - v / 100 * 10))
elif o == 2:
    print("O valor do produto fica R${:.2f}".format(v - v / 100 * 5))
elif o == 3:
    print("O valor do produto fica R${:.2f}".format(v))
elif o == 4:
    print("O valor do produto fica R${:.2f}".format(v + v / 100 * 20))