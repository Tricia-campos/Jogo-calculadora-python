def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

###Exemplo de uso da função:
peso = 70  # Peso em quilogramas
altura = 1.75  # Altura em metros

imc = calcular_imc(peso, altura)
imc