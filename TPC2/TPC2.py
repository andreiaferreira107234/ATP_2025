#Jogo dos fósforos
#Menu
def menu():
    print("Bora jogar o jogo dos fósforos!")
    print("Inicialmente, existe 21 fosforos.Cada jogador (computador ou pessoa), pode tirar entre 1 a 4 fosforos quando for a sua vez de jogar")
    print("1.Começa a  tirar os fosforos (utilizador)")
    print("2.Começa o pc a tirar os fosforos")

##Modo 1
def modo_1():
    fosforos=21
    while fosforos>1:
        jogfos=int(input("Quantos fosforos queres tirar?Escolhe entre 1 a 4 fosforos"))
        print(f"Retiraste {jogfos} fosforos.Ficaram {fosforos-jogfos} fosforos restantes")
        fosforos=fosforos-jogfos
        comp=5-jogfos
        print(f"Retiraste {comp} fosforos.Ficaram {fosforos-comp} fosforos restantes")
        fosforos=fosforos-comp
    print("Perdeste.É a tua vez e sobrou apenas 1 fósforo womp womp")

##Modo 2
def modo_2():
    fosforos=21
    while fosforos>1:
        from random import randint
        comp=randint(1,4)
        print(f"Retirei {comp}, restam {fosforos-comp} fosforos")
        fosforos=fosforos-comp
        jog=int(input(f"Agora tu, quantos fosforos queres retirar?"))
        print(f"Retiraste {jog} fosforos.Agora ficaram {fosforos-jog} fosforos restantes")
        fosforos=fosforos-jog
        if jog+comp !=5:
            comp=5-jog
            print(f"Retiraste {comp} fosforos. Ficaram {fosforos-comp} fosforos")
            fosforos=fosforos-comp
            jog=int(input(f"Agora tu, quantos fosforos queres retirar?"))
            print(f"Retiraste {jog} fosforos.Agora ficaram {fosforos-jog} fosforos restantes")
            fosforos=fosforos-jog
            while fosforos>1:
                comp=5-jog
                print(f"Retiraste {comp} fosforos. Ficaram {fosforos-comp} fosforos")
                fosforos=fosforos-comp
                jog=int(input(f"Agora tu, quantos fosforos queres retirar?"))
                print(f"Retiraste {jog} fosforos.Agora ficaram {fosforos-jog} fosforos restantes")
                fosforos=fosforos-jog
    print("Perdeste.É a tua vez e sobre 1 fosforo")

## Jogo
menu()
opcao=input("Escolha uma opção")
while opcao:
    if opcao=="1":
     modo_1()
     repetir=input("Queres voltar a jogar?")
     if repetir=="sim":
         menu()
     else:
         print("Obrigada por jogar")
    elif opcao=="2":
        modo_2()
        repetir=input("Queres voltar a jogar?")
        if repetir=="sim":
         menu()
        else:
         print("Obrigada por jogar")
print("Obrigada por jogar!!!")