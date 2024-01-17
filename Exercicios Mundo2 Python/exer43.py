a = float(input("Digite sua altura: "))
p = float(input("Digite seu peso: "))
imc = p / (a * a)
if imc < 18.5:
    print("IMC {:.2f}, Você está abaixo do peso Cuidado".format(imc))
elif imc >= 18.5 and imc < 25:
    print("IMC {:.2f}, Parabéns você esta no peso ideal".format(imc))
elif imc >= 25 and imc < 30:
    print("IMC {:.2f}, Você está sobre o peso cuide-se".format(imc))
elif imc >= 30 and imc < 40:
    print('IMC {:.2f}, Você está com obesidade cuide-se'.format(imc))
elif imc > 40:
    print('IMC {:.2f}, Você está com obesidade morbida cuide-se'.format(imc))