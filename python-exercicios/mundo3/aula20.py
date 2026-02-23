#FUNÇÕES
#Versão: Iniciante
#Linguagem: Python
#Aspectos: Funções, lista como arg, while, controle de índice, len() func, if/else, acumuladores, loop infinito, manipulação. 


#Função que Calcula Área
def area(l, c):
    a = l * c
    print(f"A área de um terreno {largura}x{comprimento} é de {a}m².")


largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
area(largura, comprimento)



#Um Print Especial
def escreva(txt):
    print('-' * len(txt))
    print(txt)
    print('-'*len(txt))


frase = str(input("Escreva uma frase: ")).strip().capitalize()
escreva(frase)



#Função de Contador
def contador(i, f, p):
    if i > f:
        for c in range(i, f-1, -p):
            print(f"{c} ",end='')
        print('FIM')

    else:
        for c in range(i, f+1, p):
            print(f"{c} ", end='')
        print('FIM')


inicio = int(input('Começo: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)



#Função que Descobre o Maior
def maior(lista):
    maior = 0
    p = 0
    while p < len(lista):
        if p == 0:
            maior = lista[p]
        else:
            if lista[p] > maior:
                maior = lista[p]
        p += 1
    print(f"O maior valor digitado foi: {maior}")


valor = []
while True:
    valor.append(int(input("Digite um valor: ")))
    while True:
        opc = str(input("Quer digitar mais valores? [S/N]: ")).upper()[0]
        if opc in 'NS':
            break
        print('ERRO, digite S ou N.')
    if opc in 'N':
        break
print()
maior(valor)



#Funções Para Sortear e Somar
from random import randint
numeros = []

def sorteia(list):
    print("Sorteado 5 valores: ", end='')
    for c in range(1,6):
        n = randint(1,10)
        print(f"[{n}] ",end='')
        list.append(n)
    print()
def somapar(list):
    soma = 0
    for i in range(len(list)):
        if list[i]%2==0:
            soma += list[i]
    print(f"Soma dos valores pares de {list}, temos {soma}")


sorteia(numeros)
somapar(numeros)