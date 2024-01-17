from datetime import date
ano = date.today().year
cm = 0
cme = 0
for c in range(1,8):
    anonasc = int(input('Digite seu ano de nascimento: '))
    if ano - anonasc >= 18:
        cm = cm + 1
    elif ano - anonasc < 18:
        cme = cme + 1
print("A quantidade de pessoas que ja atingiram a maioridade é {} e as que não atingiram é {}".format(cm,cme))
