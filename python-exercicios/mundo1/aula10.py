#CONDIÇÕES



#Condição Composta
tempo = int(input("Quantos anos tem seu carro: "))

if tempo <= 3:
    print("Carro novo.")
else:
    print("Carro velho.")
print("--FIM--")



#Condição Composta Simplificada
print('carro novo' if tempo <= 3 else 'carro velho')



#Prática00
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2) / 2
print(f"Sua média é: {media:.1f}")
if media >= 6.0:
    print("Nota boa, parabéns!")
else:
    print("Nota ruim, estude mais!")
print("--FIM--")


#Prática01
from random import randint
numeropensado = randint(0,5)
numerochutado = int(input("Adivinhe o número que o computador pensou de 0 á 5: "))
if numerochutado == numeropensado:
    print("\nParabéns, você adivinhou o número!")
else:
    print("\nQue pena, você não adivinhou o número.")
print(f"O número que o computador pensou foi {numeropensado}")


#Prática02
velocidade = int(input("Quantos Km/h o carro estáva?: "))
if velocidade > 80:
    print("Vixe, limite da via é 80km/h, ctz que foi multado!")
    multa = (velocidade - 80) * 7
    print(F"A multa vai ficar uns {multa:.2f} conto.")
else:
    print("Á ta suave, o limite da via é 80km/h, não foi multado.")


#Prática03
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Esse número é par.")
else:
    print("Esse número é impar.")


#Prática04
distanciaviagem = float(input("Quantos km tem essa viagem? -> "))
if distanciaviagem <= 200:
    valorpassagem = distanciaviagem * 0.50
    print(f"Então o valor da passagem será: R${valorpassagem:.2f}")
else:
    valorpassagem = distanciaviagem * 0.45
    print(f"Então o valor da passagem será: R${valorpassagem:.2f}") 


#Prática05
ano = int(input("Digite um ano qualquer> "))
if ano % 4 == 0:
    print(F"O ano {ano} foi um ano bissexto.")
else:
    print(f"O ano {ano} não foi um ano bissexto.")


#Prática06
n1 = int(input("Número 1> "))
n2 = int(input("Número 2> "))
n3 = int(input("Número 3> "))

if n1 > n2 and n1 > n3:
    maiornumero = n1
if n2 > n1 and n2 > n3:
    maiornumero = n2
if n3 > n1 and n3 > n2:
    maiornumero = n3

if n1 < n2 and n1 < n3:
    menornumero = n1
if n2 < n1 and n2 < n3:
    menornumero = n2
if n3 < n1 and n3 < n2:
    menornumero = n3

print(f'O maior numero digitado foi: {maiornumero}')
print(f'O menor numero digitado foi: {menornumero}')


#Prática07
salario = float(input('Qual o seu Salário? R$'))
if salario > 1250:
    aumento = salario * (10 / 100)
    salario_com_aumento = salario + aumento
    print(f"Seu salário com aumento será: R${salario_com_aumento:.2f}")

if salario <= 1250:
    aumento = salario * (15 / 100)
    salario_com_aumento = salario + aumento
    print(F"Seu salário com aumento será: R${salario_com_aumento:.2f}")


#Prática08
reta1 = int(input("Primeira reta: "))
reta2 = int(input("Segunda reta: "))
reta3 = int(input("Terceira reta: "))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print(f'Essas retas podem formar um triângulo.')
else:
    print(f'Essas retas não podem formar um triângulo.')