import random
print("*********************************")
print("***Bem vindo ao jogo da Forca!***")
print("*********************************")

continuar = 1

while continuar == 1:

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

    lista = []

    for linha in arquivo:
        linha = linha.strip()
        lista.append(linha)
    arquivo.close

    palavra_aleatoria = random.randrange (0, len(lista))
    palavra_seceta = lista [palavra_aleatoria]
    
    print(f"A palavra secreta possui {len(palavra_seceta)} letras")
    for letra in range(1):
        print("'_' "*len(palavra_seceta))
    print(palavra_seceta)

    


    break