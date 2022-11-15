import random
print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

#Define o tema
while True:

    print("Escolha um tema:")
    print("1- Objetos")
    print("2- Frutas")
    print("3- Nomes Masculino")
    print("4- Nomes Feminino")
    
    tema = int(input()) 

    if tema == 1:
        arquivo = open("Objetos.txt", "r")
    elif tema == 2:
        arquivo = open("Frutas.txt", "r")
    elif tema == 3:
        arquivo = open("Nomes Masculino.txt", "r")
    elif tema == 4:
        arquivo = open("Nomes Feminino.txt", "r")
    else:
        print("opção invalida")
        continue

#Define a palavra secreta
    lista = []

    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
    arquivo.close

    palavra_aleatoria = random.randrange (0, len(lista))
    palavra_seceta = lista [palavra_aleatoria]
    print(palavra_seceta)

    
#Inicio do jogo (quantidade de chances + print inicial da palavra oculta)
    chances = 7
    print(f"A palavra secreta possui {len(palavra_seceta)} letras.\n         E você possui {chances} chances")
    chutes_certos =  ["_"for letra in palavra_seceta]
    print(chutes_certos)


#Chuetes do usuario
    print ("digite uma letra")

    while chances >0:
        chute = input()
        chute = chute.strip().lower()
#chute certo
        if chute in palavra_seceta:
            print (f"A palavra secreta possui {chute}")
            index = 0
            for letra in palavra_seceta:
                if chute == letra:
                    chutes_certos[index] = letra
                index += 1 
            print(chutes_certos)
#chutes errado
        else:
            print(f"A palavra secreta nao possui {chute}\n      Tente de novo")
            chances -= 1
        print(f"digite uma nova letra\nAgora você possui {chances} chances")

#conferindo palavra correta
    print(palavra_seceta)
    break