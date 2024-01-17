from datetime import date
anoncm = int(input("Digite seu ano de nascimento: "))
ano = date.today().year
idade = ano - anoncm
if idade < 18:
    print("Você tem {} anos e ainda vai se alistar, falta {} para poder se alistar ".format(idade, 18 - idade))
elif idade == 18:
    print("Você tem {} anos está na hora de você se alistar".format(idade))
elif idade > 18:
    print("Você tem {} anos e ja passou {} anos do tempo de voce se alistar".format(idade, idade - 18))