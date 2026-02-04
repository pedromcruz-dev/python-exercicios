#Interrompendo repetições while
#Versão: Iniciante
#Linguagem: Python
#Aspectos: While, flags, condicionais, acumuladores/contadores, op. matemáticas, bibliotecas.

#Vários Números com Flag
ndigitados = nsoma = 0

while True:
    n = int(input("Digite um número: "))
    
    if n == 999:
        break
    
    ndigitados += 1
    nsoma += n

print(f"Foram digitados {ndigitados} e a soma deles é {nsoma}.")


#Tabuada v3.0
while True:
    valor = int(input("Quer ver a tabuada de qual valor?: "))
    i = 0

    if valor <= -1:
        print("VALOR NEGATIVO, ENCERRANDO...")
        break

    while i <= 10:
        tabuada = valor * i
        print(f"{valor} x {i} = {tabuada}")
        i += 1


#Par ou Impar
from random import choice

jvitorias = 0

while True:
# respostas jogador
    rjogador = str(input("Par ou impar?: ")).upper()
    njogador = int(input(f"Digite um número {rjogador} de 0 á 10: "))

# respostas computador
    if rjogador == "PAR": 
        rcomputador = "IMPAR"    
        ncomputador = choice(range(1, 11, 2))
    if rjogador == "IMPAR":
        rcomputador = "PAR" 
        ncomputador = choice(range(0, 11, 2))

#print das escolhas
    print(f"""\n                   ---ESCOLHAS---
          Jogador escolheu {rjogador} e jogou {njogador}.
          Computador escolheu {rcomputador} e jogou {ncomputador}\n""") 
    
#cálculo do resultado
    soma = njogador + ncomputador

    if soma % 2 == 0 and rjogador == "PAR":
        rresultado = "PAR"
        resultado = "Jogador venceu!!!"
        jvitorias += 1
    
    if soma % 2 == 1 and rjogador == "IMPAR":
        rresultado = "IMPAR"
        resultado = "Jogador venceu!!!"
        jvitorias += 1

    else: 
        rresultado = rcomputador
        resultado = "Computador venceu!!!"

#print do resultado
    print(f"""\n                   ---RESULTADO---
          A soma dos valores é {soma} que é {rresultado}.
          {resultado}\n""")

#flag
    if resultado == "Computador venceu!!!":
        vezes = "vez" if jvitorias == 1 else "vezes"
        print(f"Jogador perdeu, e conseguiu vencer {jvitorias} {vezes}, encerrando...")
        break  


#Análise de Dados em Grupo
pessoa = 1
maiordeidade = fmenorq20 = qtdhomem =  0

while True:
    
    print(f"\n---Pessoa {pessoa}---")

    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]): ")).upper()

    if idade > 18:
        maiordeidade += 1

    if idade < 20 and sexo == "F":
        fmenorq20 += 1

    if sexo == "M":
        qtdhomem += 1

    resposta = str(input("\nQuer continuar? [S/N]: ")).upper()

    if resposta == "N":
        print("Encerrando programa...")
        break

    else:
        pessoa += 1

print(F"\nForam cadastradas {maiordeidade} pessoas maior de idade.")
print(F"Foram cadastrados {qtdhomem} homens.")
print(F"Foram cadastradas {fmenorq20} mulheres menor que 20 anos.")


#Estatísticas em Produtos
print("""\n         ---LISTA DE COMPRA---""")

totalgasto = custamaisquemil = vprodutomaisbarato = agente = 0
nprodutomaisbarato = " "

while True:
    nome = str(input("\nNome do produto: ")).upper().strip()
    preco = float(input("Preço do produto: R$"))
    
    agente += 1

    totalgasto += preco

    if preco > 1000:
        custamaisquemil += 1

    if agente == 1:
        vprodutomaisbarato = preco
    elif preco < vprodutomaisbarato:
        nprodutomaisbarato = nome

    resposta = str(input("Cadastrar novo produto? [S/N]: ")).upper().strip()

    if resposta == "N":
        print("Encerrando programa...")
        break

print("\n           ---ESTASTÍSTICAS DA COMPRA---\n")

print(f"""      Total da compra: R${totalgasto:.2f}.
      Produtos que custam mais que R$1.000: {custamaisquemil}.
      Produto mais barato: {nprodutomaisbarato}.""")


#Simulador de Caixa Eletrônico
print("\n       ---CAIXA ELETRÔNICO---\n")

valorsacado = int(input("Valor de saque: R$"))
total = valorsacado
cedula = 50
totalcedula = 0

while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        print(f"Total de {totalcedula} de R${cedula}.")
        if cedula == 50: 
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        
        totalcedula = 0
    
        if total == 0:
            break
