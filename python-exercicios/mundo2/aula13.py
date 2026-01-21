#estruturas de controle
#Versão: Iniciante
#Linguagem: Python
#Conceitos usados: for/range; if/elif; op. aritméticas; comparações lógicas; contadores e acumuladores. 

# contagem regressiva com pausa
from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('feliz ano novo')

# numeros pares de 1 até 50
for i in range(1,51):
    if i % 2 == 0:
        print(i)

# soma de numeros primos e multiplos de tres
s = 0
for i in range(1,501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
        print(i)
print(f'soma de numeros primos e multiplos de 3, de 1 á 500> {s}')

#tabuada
n = int(input("Tabuada de qual número: "))
print(f"tabuada do número {n}")
for i in range(0,11):
    print(f'{n} x {i} = {i*n}')

#soma números pares e desconsidera impares
s = 0
numerospares = []
for i in range(0,6):
    numero = int(input("digite um número: "))
    if numero % 2 == 0:
        s += numero
    elif numero % 2 == 1:
        numerospares.append(numero)
print(f"soma dos números pares: {s}")
print(f"números pares desconsiderados: {numerospares}")

#PA automática
#fórmula: soma do primeiro termo com a posição do termo (ex: segundo termo) vezes a razão
primeirotermo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
for i in range(0,10):
    print(primeirotermo + (i * razao))

#número primo ou não
numero = int(input("\033[mDigite um número: "))

total = 0

for i in range(1, numero+1):

    if numero % i == 0:
        print("\033[31m", i)
        total += 1
    
    else:
        print("\033[32m", i)

if total == 2:

    print(f"""\033[mO número {numero} foi divisível {total} vezes.
Por isso ele é primo.""") 
    
else:
    print(f"""\033[mO número {numero} foi divisìvel {total} vezes.
Por isso ele não é primo.""")

#polídromo ou não
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print("Essa frase é um palíndromo.")
else:
    print("Essa frase não é um palíndromo.")

#menor idade e maior idade
nomes = []
idades = []
nomesmenor = []
nomesmaior = []

menoridade = 0
maioridade = 0

for i in range(1,8):

    nome = str(input(f"{i}o Nome: ")).strip().title()
    idade = int(input(f"Ano de nascimento: "))
    nomes.append(nome)
    idades.append(idade)

    if 2026 - idade < 18:
        menoridade += 1
        nomesmenor.append(nome)
    else:
        maioridade += 1
        nomesmaior.append(nome)

print(f"""Quantidade de pessoas menor de idade: {menoridade}
Nomes: {nomesmenor}""")
print(f"""Quantidade de pessoas maior de idade: {maioridade}
Nomes: {nomesmaior}""")

#maior peso e menor peso
peso = 0 
maiorpeso = 0
menorpeso = 0

for i in range(1,4):

    pesodigitado = float(input(f"Peso da {i}o pessoa: "))

    if i == 1:
        maiorpeso = pesodigitado
        menorpeso = pesodigitado
    else:
        if pesodigitado > maiorpeso:
            maiorpeso = pesodigitado
        if pesodigitado < menorpeso:
            menorpeso = pesodigitado

print(f"""O maior peso foi: {maiorpeso}.
O menor peso foi: {menorpeso}.""")


somaidade = 0
mediaidade = 0
nomemaisvelho = ''
maioridadehomem = 0
mulheresmenorde20 = 0

for i in range(1,4):
    print(f"----{i} PESSOA----")
    nome = str(input("Nome: ")).strip().title()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()
    
    somaidade += idade

    if i == 1 and sexo == 'M':
        maioridadehomem = idade
        nomemaisvelho = nome

    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome

    if sexo == 'F' and idade < 20:
        mulheresmenorde20 += 1

mediaidade = somaidade / 3
print(f"A média de idade do grupo é de: {mediaidade} anos.")
print(f"O homem mais velho é {nomemaisvelho} com {maioridadehomem} anos")
print(f"A quantidade de mulheres menor que 20 anos é: {mulheresmenorde20}")

