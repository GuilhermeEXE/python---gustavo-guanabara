peso = float(input("Digite seu peso: KG "))
altura = float(input("Digite sua altura: M "))
imc = peso / (altura * altura)

if imc < 18.5:
    print("ABAIXO DO PESO")
elif imc >= 18.5 and imc <= 25:
    print("PESO IDEAL")
elif imc >= 25 and imc <= 30:
    print("SOBREPESO")
elif imc >= 30 and imc <= 40:
    print("OBESIDADE")
else:
    print("OBESIDADE MORBIDA")