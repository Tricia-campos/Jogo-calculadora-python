

def calcular_imc():
    peso = float(input("Digite aqui seu peso: "))
    altura = float(input("Digite aqui sua altura: "))
    imc = peso / (altura ** 2)
    return imc

imc = calcular_imc()
print(f"O seu imc é de: {imc:.2f}")