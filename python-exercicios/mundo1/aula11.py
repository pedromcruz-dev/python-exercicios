#Cores no Terminal
#Versão: Iniciante
#Linguagem: Python
#Conceitos usados: Escape sequence, dicionário/array

#ANSI - Escape Sequence (\)
#Syntax - \033[m
#Parâmetros - [estilo; cor; fundom


cores = {'limpa':'\033[m',
         'azul':'\033[34m;',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;37;40m'}

n1 = 3
n2 = 5

print(f"Os valores são {cores['amarelo']}{n1}{cores['limpa']} e {cores['azul']}{n2}{cores['limpa']}.")