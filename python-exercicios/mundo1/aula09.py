# MANIPULAÇÃO DE TEXTO

#fatiamento

frase = 'Curso em Video Python'

print(frase[9])

print(frase[9:13])

print(frase[9:21:2])

print(frase[:5])

print(frase[15:])

print(frase[9::3])

#anlálise

print(len(frase))

print(frase.count('o'))

print(frase.count('o', 0, 13))

print(frase.find('deo'))

print(frase.find('Android'))

print('Curso'in frase)

#transformação

print(frase.replace('Python', 'Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

print(frase.strip())

print(frase.rstrip())

print(frase.lstrip())

frasesplit = frase.split()

print('-'.join(frasesplit))

print(frase.upper().count('O'))

print(frasesplit[2] [3])

#prática 0 

nome = str(input('Digite seu nome completo: ').title().strip())

print(nome.upper())

print(nome.lower())

print(len(nome)-nome.count(' '))

nomesplit = nome.split()

print(len(nomesplit[0]))

#prática 1 

numero = int(input("Digite um número: ").strip())

print(f'Unidade: {numero // 1 % 10}')

print(f'dezena: {numero // 10 % 10}')

print(f'centena: {numero // 100 % 10}')

print(f'milhar: {numero // 1000 % 10}')

#prática 2

cidade = str(input("Cidade: ").strip().capitalize())

print(f'A cidade começa com o nome Santo? {"Santo" in cidade}')

#prática 3

nome = str(input("Nome: ").strip().title())

print(F"Análisando o nome {nome}")

print(F"O nome tem Silva? {'Silva' in nome}")

#prática 4

frase = str(input("Frase: ").upper().strip())

print(f'{frase}, qtd carac: {len(frase)}')

print(f"Qtd letra A: {frase.count('A')}")

print(f"Posição 1 letra A: {frase.find('A')}")

print(f"Última posição letra A: {frase.rfind('A')}")

#prática 5

nome = str(input("Nome completo: ").strip().lower())

print(f"Ánalisando o nome: {nome}")

nomesplit = nome.split()

print(nomesplit[0].title())

print(nomesplit[-1].title())