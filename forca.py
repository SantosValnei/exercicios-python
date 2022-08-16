import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letra_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
            
        else:
          erros += 1
          print(f'Ops falta falta apenas {6-erros} tentativas')
        
        perdeu = erros == 6
        acertou = "_" not in letras_acertadas
        if(perdeu):
          print("Você perdeu!!")
          break
        if(acertou):
          print(f"Você ganhou!!, A fruta era {palavra_secreta}")
          break
        print(letras_acertadas)
      
    print("Fim do jogo")
    
    


def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
   
    
def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
        
    numero_aleartorio = random.randrange(0, len(palavras))
    
    palavra_secreta = palavras[numero_aleartorio]
    
    return palavra_secreta


def inicializa_letra_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().lower()
    
    return chute


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1




if(__name__ == '__main__'):
    jogar()
