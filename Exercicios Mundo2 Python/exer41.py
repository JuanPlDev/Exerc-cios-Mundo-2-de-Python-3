from datetime import date
i = int(input("Digite seu ano de nascimento: "))
ano = date.today().year
idade = ano - i
if idade <= 9:
    print('Você tem {} anos, a sua categoria é mirim'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, a sua categoria é infantil'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, a sua categoria é junior'.format(idade))
elif idade <= 20:
    print('Você tem {} anos, a sua categoria é sênior'.format(idade))
elif idade > 20: 
    print('Você tem {} anos, a sua categoria é master'.format(idade))