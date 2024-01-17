casa = float(input("Qual o valor da casa: "))
salario = float(input("Digite o seu salário: "))
ano = int(input("Em quantos anos vai pagar? "))
p = salario / 100 * 30
prestacao = casa / (ano * 12)
if prestacao > p:
    print("Emprestimo negado, execedeu 30 porcento do seu sálario {:.2f}, prestação da casa mensal {:.2f}".format(p, prestacao))
else:
    print("Emprestimo aprovado, 30 porcento do seu sálario {:.2f}, prestação da casa mensal {:.2f}".format(p, prestacao))