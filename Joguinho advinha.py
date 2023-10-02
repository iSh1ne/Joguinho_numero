import random
import os

erro=0
numero=random.randrange(0,100)
tentativa=int(input("Digite seu numero: "))
while(numero!=tentativa):
    os.system('cls')
    if(numero>tentativa):
        print("O numero e Maior")
    elif(numero<tentativa):
        print("numero e Menor")
    erro+=1
    tentativa=int(input("Digite seu numero: "))
print("Parabéns você acertou em " + str(erro) + " Tentativa")