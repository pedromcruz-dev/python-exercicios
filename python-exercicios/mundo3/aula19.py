#DICIONÁRIOS
#Versão: Iniciante
#Linguagem: Python
#Aspectos: Dicionários, listas, listas compostas, formatação tabelar, while, condicionais, acumuladores/contadores, op. matemáticas, bibliotecas.

#Dicionário em Python
alunos = {}
alunos['nome'] = str(input("Nome: ")).capitalize()
alunos['media'] = float(input("Média: "))
if alunos['media'] < 7:
    alunos['situacao'] = "REPROVADO"
else:
    alunos['situacao'] = "APROVADO"
for c, v in alunos.items():
    print(f" - {c} é igual á {v} - ")


#Jogo de Dados em Python
from random import randint
from operator import itemgetter
resultados = {'j1':randint(1,6),
              'j2':randint(1,6),
              'j3':randint(1,6),
              'j4':randint(1,6)}
ranking = []
print("Valores sorteados: ")
for c, v in resultados.items():
    print(f" O {c} tirou {v} no dado")
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print()
for i, j in enumerate(ranking):
    print(f"{i+1} Lugar, {j[0]} com {j[1]}. ")


#Cadastro de Trabalhador em Python
from datetime import datetime
trabalhador = {}
trabalhador['nome'] = str(input("Nome: ")).capitalize()
nasc = int(input("Data de nascimento: "))
trabalhador['idade'] = datetime.now().year - nasc
trabalhador['ctps'] = int(input("Carteira de trabalho (0 se não tiver): "))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input("Ano de contratação: "))
    trabalhador['salário'] = float(input("Salário: "))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year  )
print("-="*30)
for c, v in trabalhador.items():
    print(f" - Valor de {c} é {v} - ")


#Cadastro de Jogador de Futebol
jogador = {}
jogadores = []
golporpartida = []

while True:
    jogador['nome'] = str(input("Nome do jogador: ")).title()

    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou: "))
    c = 1
    while c <= partidas:
        golporpartida.append(int(input(f"Quantos gols na partida {c}: ")))
        c += 1

    jogador['gols'] = golporpartida[:]
    golporpartida.clear()
    jogador['totaldegols'] = sum(jogador['gols'])

    jogadores.append(jogador.copy())

    while True:
        opc = str(input("Quer continuar cadastrando? [S/N]: ")).upper()[0]
        if opc in 'SN':
            break
        print('ERRO, digite S ou N.')
    
    if opc in "N":
        break

print()
print(f"{'COD':<5} {'NOME':<15} {'GOLS':<10} {'TOTAL':>5}")
for i, d in enumerate(jogadores):
    print(f"{i:<5} {d['nome']:<15} {str(d['gols']):<10} {d['totaldegols']:>5}")
print()

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para cancelar): "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print('ERRO, jogador inválido.')
        print()
    
    print()

    for i, d in enumerate(jogadores):
        if busca == i:
            print(f"Dados do jogador {busca}: ")
            print(f"| Nome: {d['nome']} | ",end='')
            print(f"Gols: {d['totaldegols']} | ",end='')

            for ind, gol in enumerate(d['gols']):
                print(f"Partida {ind+1}: {gol} gols | ", end='')
            print()


#Unindo Dicionários e Listas
pessoa = {}
pessoas = []
idades = []
mulheres = []
acimamedia = []
cadastros = 0

while True:
    pessoa['nome'] = str(input("Nome: ")).capitalize()
    
    while True:
        pessoa['sexo'] = str(input("Sexo [F/M]: ")).upper()[0]
        if pessoa['sexo'] in "FM":
            break
        print('ERRO, digite F ou M.')
    
    pessoa['idade'] = int(input("Idade: "))
    
    idades.append(pessoa['idade'])
    
    if pessoa['sexo'] in "F":
        mulheres.append(pessoa['nome'])

    pessoas.append(pessoa.copy())
    cadastros += 1
    
    while True:
        opc = str(input("Continuar [S/N]: ")).upper()[0]
        if opc in "NS":
            break
        print('ERRO, digite S ou N.')
    if opc in 'N':
        break

media = sum(idades) / len(idades)
for i, v in enumerate(pessoas):
    if v['idade'] > media:
        acimamedia.append([v['nome'], v['idade']])

print('-='*30)

print(f"Pessoas cadastradas: {cadastros}")
print(f"Média de idades no sistema: {media:.1f}")
print("Mulheres cadastradas no sistema: ", end="")

for m in mulheres:
    print(f"[{m}] ", end='')
print()

print("Pessoas com idades acima da média: ", end='')
for i, p in enumerate(acimamedia):
    print(f"[{p[0]} com {p[1]}] ", end='')
print()
