'''
Contar uma história em Phyton
Aula 04 - Nivelamento em Programação
Por Douglas
05/08/2022
'''
import random
import termcolor
segundaAcao = random.randint(2, 11)

def acaoLeao():
    i = 0
    while segundaAcao >= i:
        print(", rugiu", sep="", end="")
        i = i + 1


leaoIdade = random.randint(18, 70)

print("\n")
termcolor.cprint("Nessa pequena história iremos contar com dois animais, um leão e um rato.", 'cyan', end=' ')
print("\nVamos pedir a sua ajuda nessa história.\033[0m")
print("\n")
leaoNome = input("Por favor, digite um nome para o nosso leão: ")
ratoNome = input("Agora, digite um nome para o nosso rato: ")
print("\n")

while leaoNome == ratoNome:
    termcolor.cprint("Por favor, nomear o nosso leão e rato com nomes diferentes", 'red', end=' ')
    leaoNome = input("\nPor favor, digite um nome para o nosso leão: ")
    ratoNome = input("E um nome diferente para o nosso rato: ")
    print("\n")
else:
    print("=" * 70)
    print(" " * 20, end="")
    print("\033[1m\033[94m+-+- O LEÃO E O RATO -+-+\033[0m")
    print("=" * 70)

    print("\nCerta vez, um leão chamado", leaoNome, "(que tinha", leaoIdade, "anos) estava dormindo na selva"
                                                                             "\nquando um rato chamado", ratoNome,
          "começou a correr para cima e para baixo"
          "\nem seu corpo apenas para se divertir.\n ")

    print("Isso perturbou o sono do poderoso leão ", leaoNome, ", e ele acordou muito zangado.\n", sep="")
    print("Ele estava prestes a comer o", ratoNome, "quando o este pediu desesperadamente que o libertasse.\n")

    primeiraAcao = random.randint(1, 11)

    if primeiraAcao % 2:
        print("\033[1;31mO leão decidiu que iria devorar o rato desocupado\033[0m")
    else:
        print("\033[93mO leão decidiu que não iria comer o rato desocupado\033[0m")
        print("'Eu prometo a você, um dia serei de grande ajuda se você me perdoar.', comentou o", ratoNome, "\n",
              leaoNome, "riu da confiança daquele minúsculo ser e o deixou ir.\n")

    print("Um dia, alguns caçadores entraram na floresta e levaram o leão com eles.\n")

    print("Eles o amarraram contra uma árvore. O ", leaoNome, " estava lutando e ele", sep="", end="")

    print(acaoLeao())

    if primeiraAcao % 2:
        print(".\nO leão que estava sem amigos na floresta acabou por morrer de fome, preso a árvore", sep="")
        print("\033[1;31mMoral da história: algumas vezes relevar um pequeno ato pode salvar sua vida")
    else:
        print(".\nLogo,", ratoNome, " passou e notou o leão em apuros. Rapidamente, ele correu e roeu as cordas para \n"
                                 "libertar o leão. Os dois correram e o leão ficou livre.\n", sep="")
        print("\033[93mMoral da história: Um pequeno \033[1mato de gentileza pode ajudar muito.\033[0m")
