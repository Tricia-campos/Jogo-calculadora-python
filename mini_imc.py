

def calcular_imc():
    peso = float(input("Digite aqui seu peso: "))
    altura = float(input("Digite aqui sua altura: "))
    imc = peso / (altura ** 2)
    return imc

abaixo = 18.5
normal = 24.9
sobrepeso = 29.9
obeso = 34.9

imc = calcular_imc()

if imc <= 18.5:
    print("você esta abaixo do peso")
elif imc <= 24.9:
    print("você esta com o peso normal")
elif imc <= 29.9:
    print("você esta acima do peso")
else:
    imc >= 34.9
    print("você esta obeso")


print(f"O seu imc é de: {imc:.2f}")