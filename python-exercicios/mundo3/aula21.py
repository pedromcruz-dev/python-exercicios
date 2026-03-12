#FUNÇÕES PT.2
#Versão: Iniciante
#Linguagem: Python
#Aspectos: Funções, lista como arg, while, controle de índice, len() func, if/else, acumuladores, loop infinito, manipulação.


#Funções para Votação
from datetime import datetime

def voto(anonasc=0):
    """
    -> Retorna sua condição de voto eleitoral baseando-se no ano de nascimento.
    anonasc param: Int value
    return: String value 
    """
    
    idade = datetime.today().year - anonasc
    print(f"Com {idade} anos: ", end='')
    if idade < 16:  
        return 'NEGADO'
    elif 16 <= idade < 18:
        return 'OPCIONAL'
    else: 
        return 'OBRIGATÓRIO'
    
help(voto)
ano = int(input("Digite seu ano de nascimento: "))
retorno = voto(ano)
print(f"VOTO {retorno}")




#Função para Fatorial
def fatorial(n,show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: (OPCIONAL) mostrar ou não a conta
    :return: O valor do fatoria de um número (n)
    """
    resultado = 1
    if show == True:
        for i in range(n, 0, -1):
            print(f"{i}", end='')
            print(" x " if i > 1 else " = ", end='')
            resultado *= i
        return resultado
    else:
        for i in range(n, 0, -1):
            resultado *= i
        return resultado

valor = int(input("Fatorial de qual valor?: "))

while True:
    resposta = str(input("Quer que mostre a conta? [S/N]: ")).upper()[0]
    if resposta == "S":
        opc = True
        break
    elif resposta == "N":
        opc = False
        break
    else:
        print("ERRO, digite S ou N.")

help(fatorial)
print(f"Fatorial do valor {valor}: ", end='')
print(fatorial(valor, opc))




#Ficha do Jogador
def ficha(n='<desconhecido>', g=0):
    print(f"O jogador {n} fez {g} gols no campeonato.")


nome = str(input("Nome do Jogador: ")).title().strip()
gols = input("Número de gol(s): ")

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if nome.strip() == "":
    ficha(g=gols)
else:
    ficha(nome, gols)




#Validando Dados de Entrada em Python
def leiaint(msg):
    ok = False
    valorvalidado = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valorvalidado = n
            ok = True
        else:
            print('\033[31mERRO, Digite um número INTEIRO.\033[m')

        if ok:
            break
    return valorvalidado

n = leiaint("Quer validar qual número?: número ")
print(f"\033[32mO número {n} foi VALIDADO.\033[m")




#Analisando e Gerando Dicionários
def notas(*nota, sit=False):
    informacoes = {}
    informacoes['Notas'] = len(nota)
    informacoes['Maior nota'] = max(nota)
    informacoes['Menor nota'] = min(nota)
    informacoes['média'] = round(sum(nota) / len(nota), 2)
    
    situacao = ''
    if sit == True:
        if informacoes['média'] <= 5:
            situacao = 'RUIM'
        elif informacoes['média'] <= 7:
            situacao = 'RAZOÁVEL'
        else:
            situacao = 'ÓTIMA'
        informacoes['sit'] = situacao

    return informacoes
    
print(notas(4.5, 6.7, 10, sit=True))




#Sistema Interativo de Ajuda em Python
def ajuda(c):
    help(c)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP')
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!')