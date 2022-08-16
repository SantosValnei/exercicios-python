import advinhacao
import forca

print('*' * 30)
print('*** Escolha o Jogo ***')
print('*' * 30)

print('Escolha (1) Advinhacao ou (2) Forca')
jogo = int(input('Qual o jogo desejar jogar? '))

if(jogo == 1):
    advinhacao.jogar()
elif(jogo == 2):
    forca.jogar()