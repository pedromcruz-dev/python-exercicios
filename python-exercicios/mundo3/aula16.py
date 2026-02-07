#Tuplas
#Versão: Iniciante
#Linguagem: Python
#Aspectos: Tuplas,formatação tabelar, while, condicionais, acumuladores/contadores, op. matemáticas, bibliotecas.


#Número por Extenso
zeroavinte = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:

    numero = int(input("Digite um número entre 0 e 20: "))

    if 0 <= numero <= 20:
        print(f"Você digitou o número: {zeroavinte[numero].upper()}\n")

    else:
        print("Tente novamente. ", end='')


#Tuplas com Time de Futebol
vinteprimeiros = ('bragantino', 'palmeiras', 'chapecoense', 'mirassol', 'bahia', 'fluminense', 'são paulo', 'botafogo', 'grêmio', 'paranaense', 'coritiba', 'vitória', 'atlético mineiro', 'flamengo', 'vasco', 'internacional', 'santos', 'clube do remo', 'corinthians', 'cruzeiro')

print(f"Os 5 primeiros colocados são: {vinteprimeiros[0:6]}")
print(f"Os 4 últimos colocados são: {vinteprimeiros[16:]}")

ordem = sorted(vinteprimeiros)
print(ordem)

posichapeco = vinteprimeiros.index('chapecoense') + 1
print(f"Chapecoense na {posichapeco}a posição' da tabela")


#Maior e Menor Valores em Tupla
from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

menornumero = numeros[0]
maiornumero = numeros[0]

for numero in numeros:
    
    if numero < menornumero:
        menornumero = numero

    if numero > maiornumero:
        maiornumero = numero

    numero += 1

print(f"A lista de números sorteados é: {numeros}")
print(f"O menor número sorteado foi: {menornumero}")
print(f"O maior número sorteado foi: {maiornumero}")


#Análise de Dados em uma Tupla
valores = ()

valor9 = 0

valor3 = 0

valorpar = ()

for i in range(1,5):

    valor = int(input("Digite um valor: "))

    if valor == 9:
        valor9 += 1

    if valor % 2 == 0:
        valorpar += (valor,)

    valores += (valor,)

    if valor == 3:
        valor3 += valores.index(3)

    i += 1

print(f"Os valores digitados foram: {valores}")
print(f"O valor 9 apareceu {valor9} vezes.")
print(f"O valor 3 apareceu na posição: {valor3+1}")
print(f"Os valores pares são: {valorpar}")


#Lista de Preços com Tupla
produtos = ("Arroz", 49.99, "Feijão", 47.99, "Bis", 5.99)

print("PRODUTO | PREÇO")
print("-"*15)

for produto in range(0, len(produtos), 2):
    print(f"{produtos[produto]:^7} | {produtos[produto+1]:^7}")


#Contando Vogais em Tupla
palavras = ("ola", "farelo", "aleluia", "recussitou", "sempre")

for palavra in palavras:

    print(f"\nNa palavra {palavra.upper()} temos ",end='')

    for letra in palavra:

        if letra in "aeiou":

            print(f"{letra} ", end='')
