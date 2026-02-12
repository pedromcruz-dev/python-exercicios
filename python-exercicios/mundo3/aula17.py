#Listas
#Versão: Iniciante
#Linguagem: Python
#Aspectos: Listas,formatação tabelar, while, condicionais, acumuladores/contadores, op. matemáticas, bibliotecas.


#Maior e Menor Valores da Lista
valores = []

maior = 0

menor = 0

for p in range(0,5):
    
    valores.append(int(input(f"Digite um valor para a posição {p}: ")))

    if p == 0:

        maior = menor = valores[p]

    else:
        
        if valores[p] > maior:

            maior = valores[p]

        if valores[p] < menor:

            menor = valores[p]

print(f"A LISTA é: {valores}")

print(f"O MAIOR valor da lista é {maior} na posição ", end='')

for p, v in enumerate(valores):
    
    if v == maior:

        print(f"{p}, ", end='')

print()

print(f"O MENOR valor da lista é {menor} na posição ", end='')

for p, v in enumerate(valores):

    if v == menor:
        
        print(f"{p}, ")

print()


#Valores Únicos em uma Lista
valor = []

while True:

    v = int(input("Digite um valor: "))

    if v in valor:
       
       print("Valor já digitado, não vou adicionar.")

    if v not in valor:
        
        print("Valor adicionado com sucesso.")
        
        valor.append(v)

    resposta = str(input("Quer continuar? [S/N]: ")).upper()
        
    if resposta == "N":
        
        print("Encerrando programa.")

        break

print(f"Os valores digitados foram: {sorted(valor)}")


#Lista Ordenada sem Repetições
valores = []

for p in range(0,5):

    v = int(input("Digite um valor: "))

    if p == 0 or v > valores[-1]:

        valores.append(v)

        print("Adicionado na última posição da lista.")

    else: 
        p = 0
        
        while p < len(valores):

            if v <= valores[p]:

                    valores.insert(p, v)
                    print(f"Adicionado na posição {p} da lista.")
                    break
            
            p += 1
        
print(f"A lista já em ordem é: {valores}")


#Extraindo Dados de uma Lista
numeros = []

numerosdigitados = 0

while True:

    numero = int(input("Digite um número: "))

    numeros.append(numero)

    numerosdigitados += 1

    resposta = str(input("Quer continuar? [S/N]: ")).upper()
    if resposta == "N":
        break

valor5 = "SIM" if 5 in numeros else "NÃO"

print("=-" * 30)

numeros.sort(reverse=True)

print(f"A quantiades de números digitados foram: {numerosdigitados} ")
print(f"A lista ordenada de forma DECRESCENTE é: {numeros} ")
print(f"O valor 5 está na lista? {valor5}")


#Dividindo Valores em Várias Listas
numeros = []
numerospares = []
numerosimpares = []

while True:

    numeros.append(int(input("Digite um número: ")))
    
    resposta = str(input("Continuar? [S/N]: ")).upper()
    if resposta in "N":
        break

for n in numeros:
    if n % 2 == 0:
        numerospares.append(n)
    elif n % 2 == 1:
        numerosimpares.append(n)

print("=-" * 30)

print(f"Lista de números digitos: {numeros}")
print(f"Lista de números pares digitados: {numerospares}")
print(f"Lista de números ímpares digitados: {numerosimpares}")


#Validando Expressões Matemáticas
expressao = (str(input("Digite uma expressão: ")))

pilha = []

for carac in expressao:
    if carac == "(":
        pilha.append("(")
    elif carac == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

print()    

if pilha == 0:
    print("A expressão é VÁLIDA!")
else:
    print("A expressão é INVÁLIDA!")
