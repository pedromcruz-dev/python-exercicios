#Estrutua de repetição while
#Versão: Iniciante
#Linguagem: Python
#Conceitos usados: while/for/range; if/elif; op. aritméticas; comparações lógicas; contadores e acumuladores. 

#validação de dados
sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
while sexo not in ('FM'):
    if sexo != "F" or "M":
        sexo = str(input("Sexo inválido, digite novamente [M/F]: ")).upper().strip()[0]
if sexo == "M":
    print("Sexo masculino regristrado.")
elif sexo == "F":
    print("Sexo feminino registrado.")

#Adivinhação v2.0
from random import randint
numeropensado = randint(1,5)
numerochutado = int(input("Tente adivinhar o número de 1 á 5: "))

while numeropensado != numerochutado:
    numerochutado = int(input("Numero errado, tente novamente: "))

print(f"O número pensado foi {numeropensado}, você acertou.")

#menu de opções
primeirovalor = int(input("Primeiro valor: "))
segundovalor = int(input("Segundo valor: "))
opcao = 0

while opcao != 5:
    
    print("""   ---OPÇÕES---
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair """)
    opcao = int(input("    Opção: "))

    maior = 0 

    if opcao == 1:
        soma = primeirovalor + segundovalor
        print(f"A soma dos valores [{primeirovalor}] + [{segundovalor}] é [{soma}].") 

    elif opcao == 2:
        multiplicacao = primeirovalor * segundovalor
        print(f"O produto entre {primeirovalor} x {segundovalor} é {multiplicacao}.")
        
    elif opcao == 3:
        if primeirovalor > segundovalor:
            maior += primeirovalor
        elif primeirovalor < segundovalor:
            maior += segundovalor
        print(f"O maior número digitado foi {maior}")
       
    elif opcao == 4:
        primeirovalor = int(input("Digite o novo primeiro valor: "))
        segundovalor = int(input("Digite o novo segundo valor: "))

    elif opcao == 5:
        print("Encerrando programa...")

    else: 
        print("Opção inválida, tente novamente")
       

#fatorial
n = int(input("Digite um número: "))
i = n
f = 1
print(f"Calculando {n}! = ", end='')

while i > 0:
    print(i, end='')
    print(f" x " if i > 1 else " = ",end='')
    f *= i
    i -= 1

print(f)

#fatorial com for
n = int(input("Digite um número: "))
f = 1
print(f"calculando {n}! = ", end='')

for i in range(n, 0, -1):
    print(i, end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i

print(f)

#PA com while v1.0
pt = int(input("Primeiro termo: "))
r = int(input("Razão: ")) 
i = 1
print(f"{pt} -> ", end='')
while i < 10: 
    pa = pt + (i * r)
    print(f"{pa} -> ", end='')
    i += 1
print("ACABOU")

#PA com while v2.0
pt = int(input("Primeiro termo: "))
r = int(input("Razão: ")) 
i = 1

print(f"{pt} -> ", end='')
while i < 10: 
    pa = pt + (i * r)
    print(f"{pa} -> ", end='')
    i += 1
print("PAUSA")

resp = int(input("Quer mostrar mais quantos termos?: "))

while True:  
    if resp == 0:
        break

    c = 0 
    while c < resp:
        pa += r
        print(f"{pa} -> ", end='')
        c += 1
    print("PAUSA")
    resp = int(input("\nQuer mostrar mais quantos termos?: "))

print("Encerrando...")

#fibonacci (cada termo é a soma dos dois anteriores)
t = int(input("Quantos termos voce quer mostrar?: "))

c = 3
t1 = 0
t2 = 1
print(f"{t1} -> {t2} -> ", end='')

while c <= t:
    t3 = t1 + t2
    print(f"{t3} -> ", end='')
    t1 = t2
    t2 = t3
    c += 1
print("FIM")

#tratando num
i = 0
n = 0
s = 0
while i != 999:
    i = int(input("Digite um número ou 999 para encerrar: "))
    if i != 999:
        n += 1
        s += i
print(f"""
Foram digitados {n} números.
E a soma entre eles foi: {s}.
""")

#maior e menor
r = ''
s = 0
q = 0

n = int(input("Digite um número inteiro: "))

maior = n
menor = n

r = str(input("Quer continuar? [S/N]: ")).upper()


while r != "N":
    n = int(input("Digite um número inteiro: "))
    s += n
    q += 1

    if n > maior:
        maior = n
    
    if n < menor: 
        menor = n 

    r = str(input("Quer continuar? [S/N]: ")).upper()

m = s / q

print(
f"""
A média entre os valores digitados é: {m}.
O maior número digitado foi: {maior}.
O menor número digitado foi: {menor}.
""")
