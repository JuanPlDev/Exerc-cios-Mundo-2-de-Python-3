a = 0
v = 0
m = 0
for c in range(1,5):
    print("------{}ª Pessoa-----".format(c))
    n = str(input('Digite o seu nome: '))
    i = int(input('Digite a sua idade: '))
    a += i
    if i > v:
        v = i
        nomemvelho = n
    s = str(input('Sexo [M/F] ')).upper()
    if s == 'F' and i < 20:
        m = m + 1

print("A media da idade é {:.2f}".format(a/4))
print("O homem mais velho tem {} anos e se chama {}".format(v,nomemvelho))
print("Apenas {} mulher tem menos doque 20 anos".format(m))
