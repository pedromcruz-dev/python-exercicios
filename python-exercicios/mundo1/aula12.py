#Condições Aninhadas
#Versão: Iniciante
#Linguagem: Python
#Conceitos usados: if/else, operações aritméticas, biblioteca (random), funções nativas (bin, oct, hex)

#Financiamento de um imóvel
valordacasa = float(input("Valor da casa: "))
salariodocomprador = float(input("Salario do comprador: "))
quantosanos = int(input("Quantos anos vai demorar pra pagar: "))

prestacaomensal = valordacasa / (quantosanos * 12)
trintaporcento = salariodocomprador * 0.30

if prestacaomensal > trintaporcento:
    print("Financiamento negado.")
else:
    print("Financiamento aprovado.")


#Conversor binário
numerointeiro = int(input("Digite um número inteiro qualquer: "))

print("""
--Qual será a base da conversão?--
    1- para binário
    2- para octal
    3- para hexadecimal
    """)

resposta = int(input("--Digite aqui: "))

if resposta == 1:
    conversaobinario = bin(numerointeiro)
    print(f"\nO número inteiro {numerointeiro} convertido para binário é: {conversaobinario[2:]}")

elif resposta == 2:
    conversaooctal = oct(numerointeiro)
    print(f"\nO número inteiro {numerointeiro} convertido para octal é: {conversaooctal[2:]}")

elif resposta == 3:
    conversaohexa = hex(numerointeiro)
    print(f"\nO numero inteiro {numerointeiro} convertido para hexadecimal é: {conversaohexa[2:]}")

else:
    print("\nOpção não existente.")


#Comparador numérico
primeirovalor = int(input("Digite o primeiro valor: "))
segundovalor = int(input("Digite o segundo valor: "))

if primeirovalor > segundovalor:
    print(f"O primeiro valor ({primeirovalor}) é maior.")

elif segundovalor > primeirovalor:
    print(f"O segundo valor ({segundovalor}) é o maior.")

elif primeirovalor == segundovalor:
    print(f"Não existe valor maior. Os dois valores ({primeirovalor}/{segundovalor}) são iguais.")


#Tempo para o alistamento
anoatual = int(input("Qual é o ano atual: "))
anodenascimento = int(input("Em que ano nasceu: "))

idadedojovem = anoatual - anodenascimento
idadedealistamento = 18

if idadedojovem < idadedealistamento:
    anosrestante = idadedealistamento - idadedojovem
    print(f"Com {idadedojovem} anos ainda não é o momento de se alistar ao exército. Falta {anosrestante} anos.")
    
elif idadedojovem == idadedealistamento:
    print(f"Com {idadedojovem} anos é o momento certo para se alistar.")

elif idadedojovem > idadedealistamento:
    atraso = idadedojovem - idadedealistamento
    print(f"Com {idadedojovem} anos já passou da hora de se alistar. Está atrasado {atraso} anos.")
    

#Aprovado ou reprovado
primeiranota = float(input("Primeira nota: "))
segundanota = float(input("Segunda nota: "))
media = (primeiranota + segundanota) / 2

if media < 5.0:
    print(f"Sua média foi \033[31m{media}\033[m, \033[31mREPROVADO\033[m. ")

elif 5.0 <= media <= 6.9:
    print(f"Sua média foi \033[33m{media}\033[m, \033[33mRECUPERAÇÃO\033[m.")

elif 7.0 >= media:
    print(f"Sua média foi \033[32m{media}\033[m, \033[32mAPROVADO\033[m.")


#Categorização de atletas
anoatual = int(input("Ano atual: "))
anodenascimento = int(input("Atleta 1 - Ano de nascimento: "))
idade = anoatual - anodenascimento

categoriamirim = 9
categoriainfantil = 14
categoriajunior = 19
categoriasenior = 20
categoriamaster = 21

if idade <= categoriamirim:
    print(f"Atleta 1 com {idade} anos, localiza na categoria mirim.")

elif idade <= categoriainfantil:
    print(f"Atleta 1 com {idade} anos, localiza na categoria infantil.")

elif idade <= categoriajunior:
    print(f"Atleta 1 com {idade} anos, localiza na categoria junior.")

elif idade <= categoriasenior:
    print(f"Atleta 1 com {idade} anos, localiza na categoria senior.")

else:
    print(f"Atleta 1 com {idade} anos, localiza na categoria master.")


#Pode formar um triangulo e qual triangulo
primeirareta = float(input("Primeira reta: "))
segundareta = float(input("Segunda reta: "))
terceirareta = float(input("Terceira reta: "))

if primeirareta + segundareta > terceirareta and segundareta + primeirareta > terceirareta and terceirareta + primeirareta > segundareta:
    print(f"Com essas três retas ({primeirareta}, {segundareta} e {terceirareta}) PODE-SE formar um triângulo.")
    
    if primeirareta == segundareta == terceirareta:
        print("E será um triângulo EQUILATERO.")

    elif primeirareta == segundareta or primeirareta == terceirareta or segundareta == terceirareta:
        print("E será um triângulo ISÓSCELES")

    elif primeirareta != segundareta != terceirareta:
        print("E será um triângulo ESCALENO.")

else:
    print(f"Com essas três retas ({primeirareta}, {segundareta} e {terceirareta}) NÃO PODEM formar um triângulo.")


#Cálculo IMC
peso = float(input("Peso: "))
altura = float(input("Altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso.")

elif 18.5 <= imc < 25:
    print("Peso ideal.")

elif 25 <= imc < 30:
    print("Sobrepeso.")

elif 30 <= imc < 40:
    print("Obesidade.")

else:
    print("Obesidade mórbida.")


#Juros ou desconto no pagamento
preconormal = float(input("Valor do produto: R$"))

print("""
Formas de pagamento:
1 - á vista dinheiro/cheque (10% desconto)
2 - á vista cartão (5% desconto)
3 - 2x no cartão (valor normal)
4 - 3x ou mais no cartão (20% de juros)""")

resposta = int(input("Digite a opção: "))

if resposta == 1:
    valordacompra = preconormal - (preconormal * 0.10)
    print(f"\nSua compra com 10% de desconto ficou: R${valordacompra:.2f}")

elif resposta == 2:
    valordacompra = preconormal - (preconormal * 0.05)
    print(f"\nO valor da compra com 5% de desconto ficou: R${valordacompra:.2f}")

elif resposta == 3:
    valorparcelas = preconormal / 2
    print(f"\nSua compra sem desconto parcelada em 2x de R${valorparcelas:.2f} ficou: R${preconormal:.2f}")

elif resposta == 4:
    parcelas = int(input("Quantas parcelas: "))
    valordacompra = preconormal + (preconormal * 0.20)
    valorparcelas = valordacompra / parcelas
    print(f"""
    RECIBO      
    Valor parcelas: {parcelas}x R${valorparcelas:.2f} 
    Valor total: R${valordacompra:.2f}""")

else:
    print("\nOpção inexistente.")


#Jokenpô
from random import choice

opcoes = ['pedra', 'papel', 'tesoura']

jogador = str(input("Pedra, papel ou tesoura: ").lower())
computador = choice(opcoes)

print(f"Você escolheu: {jogador}")
print(f"Computador escolheu: {computador}")

if jogador == computador:
    print("Empate.")

elif (
    (jogador == "pedra" and computador == "tesoura") or
    (jogador == "tesoura" and computador == "papel") or
    (jogador == "papel" and computador == "pedra")
):
    print("Jogador ganhou.")

else:
    print("Computador ganhou.")