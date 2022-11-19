import Advinhacao
import Cartas_21
import Forca
import Jokenpo
import Simulador_de_Dados

print("*********************************")
print("*********Menu de seleção*********")
print("*********************************")

print ("Jogos disponiveis:\n 1- Adivinhação\n 2- Cartas 21\n 3- Forca \n 4- Jokenpo\n 5- Simulador de dados")
op = int(input("Selecione uma Opção: "))

if op == 1:
    print ("Selecionado Opção 1:\n Jogo de Adivinhação")
    Advinhacao.adivinhacao()
elif op == 2:
    Cartas_21.cartas()
elif op == 3:
    Forca.forca()
elif op == 4:
    Jokenpo.jokenpo()
elif op == 5:
    Simulador_de_Dados.dados()