#jogo advinhação numeros
import random

cont = 7
numero_secreto = random.randint(0, 100)
numero_int = range(0,101)
numeros_str = [str(num) for num in numero_int]

print("Olá, bem vindo ao jogo de advinhação de números")

while cont > 0:
    pergunta = (f"Você tem apenas {cont} chances, digite um número de 0 a 100: ")
    numero = (input(pergunta))
    if numero in numeros_str:
        numero = int(numero)
        if 0 <= numero <= 100:
           if numero == numero_secreto:
              print("parabens, você acertou!!!!!!!!")
              break
           elif numero > numero_secreto:
              print("O numero mistérioso é menor")
              cont = cont - 1
           else:
              print("o numero mistérioso é maior")
              cont = cont - 1
        else:
            print("Digite um numero entre 0 e 100")
    else:
           print("Digite um número entre 0 e 100, porfavor")
    if cont == 0:
      print(f"""Você perdeu
      o numero secreto era: {numero_secreto} """)