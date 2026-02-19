#Tuplas Parte 2 (Lista Composta (Matriz))
#Versão: Iniciante
#Linguagem: Python
#Aspectos: Listas,listas compostas, matriz, formatação tabelar, while, condicionais, acumuladores/contadores, op. matemáticas, bibliotecas.


# #Lista Composta e Análise de Dados
# dados = list()
# cadastros = list()
# maiorpeso = menorpeso = qtdcadastros = 0

# while True:
#     dados.append(str(input("Nome: ").title().strip()))
#     dados.append(float(input("Peso [Kg]: ")))
    
#     if len(cadastros) == 0:
#         maiorpeso = dados[1]
#         menorpeso = dados[1]
#     else:
#         if dados[1] > maiorpeso:
#             maiorpeso = dados[1]
#         if dados[1] < menorpeso:
#             menorpeso = dados[1]
    
#     cadastros.append(dados[:])
#     dados.clear()
#     qtdcadastros += 1

#     print()
    
#     resposta = str(input("Continuar cadastrando? [S/N]: "))
#     if resposta in "Nn":
#         break
    
#     print()

# print(f"Ao todo, {qtdcadastros} foram cadastradas.")

# print(f"O maior peso foi de {maiorpeso}Kg, peso de ", end='')
# for p in cadastros:
#     if p[1] == maiorpeso:
#         print(f"[{p[0]}] ", end='')
# print()

# print(f"O menor peso foi de {menorpeso}Kg, peso de ", end='')
# for p in cadastros:
#     if p[1] == menorpeso:
#         print(f"[{p[0]}] ", end='')


# #Listas com Pares e ímpares
# valores= [[], []]
# valor = 0

# for cont in range(0,7):
#     valor = (int(input("Digite um número: ")))
    
#     if valor % 2 == 0:
#         valores[0].append(valor)
#     else:
#         valores[1].append(valor)

# valores[0].sort()
# valores[1].sort()

# print(f"Os valores PARES digitados em ordem crescente são: {valores[0]}")
# print(f"Os valores ÍMPARES digitados em ordem crescente são: {valores[1]}")


# #Matriz em Python
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# par = terceiracolun = 0
# maiorvalorsegundalinha = 0

# for l in range(0,3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f"Digite um valor para a posição {l, c}: "))
            
#         if l == 1:    
#             maiorvalorsegundalinha= matriz[l][c]

# for l in range(0,3):
#     for c in range(0,3):
        
#         if matriz[l][c] % 2 == 0:
#             par += matriz[l][c]

#         if c == 2:
#             terceiracolun += matriz[l][c]

#         if l == 1:
#             if matriz[l][c] > maiorvalorsegundalinha:
#                 maiorvalorsegundalinha = matriz[l][c]
# print()

# for l in range(0,3):
#     for c in range(0,3):
#         print(f'[{matriz[l][c]}]', end='')
#     print()

# print(f"Soma dos pares digitados: {par}")
# print(f"A soma da terceira coluna é: {terceiracolun}")
# print(f"O maior valor da segunda linha é: {maiorvalorsegundalinha}")


# #Mega Sena
# from random import randint
# lista = list() #lista comum
# jogos = list() #lista composta

# quant = int(input("Quantos jogos você quer que eu sorteie?: "))
# tot = 1

# while tot <= quant:
#     cont = 0
#     while True:
#         num = randint(1,60)
#         if num not in lista:
#             lista.append(num)
#             cont += 1
#         if cont >= 6:
#             break
#     lista.sort()
#     jogos.append(lista[:])
#     lista.clear()
#     tot += 1
# print("-=" * 30)

# for i, l in enumerate(jogos):
#     print(f"Jogo {i+1}: {l}")


# #Boletim com Listas Compostas  
# alunos = list()

# while True:
#     nome = str(input("Nome: "))
#     nota1 = float(input("Nota 1: "))
#     nota2 = float(input("Nota 2: "))
    
#     m = (nota1 + nota2) / 2

#     alunos.append([nome, [nota1, nota2,], m ])
    
#     r = str(input("Continuar? [S/N]: "))
#     if r in 'Nn':
#         break

# print("--- BOLETIM ---")
# print()

# print("No.  Nome      Média")
# print("-" * 20)
# for i, l in enumerate(alunos):
#     print(f"{i:<4} {l[0]:<10} {l[2]:>.2f}")
# print()

# while True:
#     r = int(input("Quer ver as notas de qual alunos? [999 para interromper]: "))

#     for i, l in enumerate(alunos):
#         if r == i:
#             print(f"Notas de {l[0]} são {l[1]}")
#             print()

#     if r == 999:
#         print("ENCERRANDO PROGRAMA...")
#         break
