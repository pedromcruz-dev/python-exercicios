#Bibliotecas / Módulos

#exerc 1
from math import floor
n = float(input("Digite um númeor real: "))

print(f"A parte inteira de {n} é {floor(n)}")



#exerc 2
from math import sqrt
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hipo = sqrt(co**2 + ca**2)

print(f"A hipotenusa é {"hipo":.2f}.")



#exerc 3
import math
angulo = float(input("Angulo: "))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f"""
Angulo = {angulo}
Seno = {math.ceil(seno)}
Cosseno = {math.ceil(cosseno)}
Tangente = {math.ceil(tangente)}
""")


#exerc 4 
import random
alunos = ["Pedro","João", "Rafael", "Victor"]
sorteio = random.choice(alunos)

print (f"Aluno sorteado foi {sorteio}.")



#exerc 5 
alunos = ["Pedro","João", "Rafael", "Victor"]
random.shuffle(alunos)

print(f"Alunos sorteados {alunos}.")


#exerc 6
import pygame
pygame.init()
pygame.mixer.music.load(r"C:\Users\conta\OneDrive\Documentos\Aulas Guanabara\Guzman{Gly2szOBF5s].mp3")
pygame.mixer.music.play()

input("Pressione Enter para parar...")