n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) / 2
if media < 5:
    print("Sua média é {}, O aluno está reprovado".format(media))
elif media >= 5 and media < 7:
    print("Sua média é {}, O aluno está de recuperação".format(media))
elif media >= 7 :
    print("Sua média é {}, Parabéns o aluno está aprovado".format(media))