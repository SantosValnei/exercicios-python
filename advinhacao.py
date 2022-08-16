import random

def jogar():
    numero_secreto = random.randrange(1, 51)
    total_tentativas = 0
    pontos = 100
    
    print('Você está jogando Advinhacao\n')

    print('Qual nivel de dificuldade deseja? (1) Fácil (2) Medio (3) Dificil')
    nivel_dificuldade = int(input('Digite o numero para escolher o nivel: '))

    if(nivel_dificuldade == 1):
        total_tentativas = 15
    elif(nivel_dificuldade == 2):
        total_tentativas = 10
    elif(nivel_dificuldade == 3):
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print(f'Total de tentativas {rodada} de {total_tentativas}')
        chute = int(input('Digite seu numero entre 1 e 50: '))
        
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        
        if(chute < 1 or chute > 100):
            print('O numero deve ser entre 1 e 50')
            continue
        
        if(acertou):
            print(f'Você acertou e fez {pontos}')
            break
        else:
            if(maior):
                print('O seu chute foi maior que o numero secreto')
            elif(menor):
                print('O seu chute foi menor que o numero secreto')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos



    print(f'Fim de jogo!! {numero_secreto}')
    
if(__name__ == '__main__'):
    jogar()