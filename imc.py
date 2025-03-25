#IMC If
nome = input("Olá, bem vindo ao medidor de IMC, por gentileza, se identifique: ")
peso = float(input(f"{nome}, insira seu peso: "))
altura = float(input("Agora, sua altura: "))
imc = peso / altura ** 2
print("Seu IMC é de: %.2f" %imc)

if imc < 18.4:
    print("Você está abaixo do peso :(")
elif imc >= 18.5 and imc <= 24.9:
    print("Parabens, você está com o peso normal")
elif imc >= 25.0 and imc <= 29.9:
    print("atenção, você está com sobrepeso")
elif imc >= 30.0 and imc <= 34.9:
    print("Obesidade grau I")
elif imc >= 35.0 and imc <= 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")