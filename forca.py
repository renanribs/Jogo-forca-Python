def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "renan".upper()
    letras_acertadas= ["_" for letra in palavra_secreta]

    enforcou = False
    acertou  = False
    erros = 0
    falta = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):
        print("Você possui {} tentativas".format(falta))
        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            falta -= 1


        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!!!")
    else:
        print("Você perdeu! :(")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
