#Modelo do cinema
#cinema= [sala]
#sala = [nlugares,vendidos,filme]
#filme= string
#nlugares=int
#vendidos=[int]

cinema=[]
def criarsala(cinema):
    lugarestotais=int(input("Quantos lugares deseja ter na sala?"))
    nbilhetesvendidos=0
    filme=input("Qual é o filme que seja assistir?")
    filme=filme.capitalize()
    sala=[lugarestotais,nbilhetesvendidos,filme]
    cinema.append(sala)

def removersalas(cinema):
    index=int(input("Introduz o indice da sala"))
    cinema.pop(index)
    print("Sala removida")
    print("Salas:",cinema)
    menu()

def listarsalas(cinema):
    for s in cinema:
        print(s)

def lugaresdisponiveis(cinema,filme):
    for s  in cinema:
        if s[2]==filme:
            Nr=s[0]-s[1]
            return Nr
    return False


def venderbilhete(cinema,filme,nbilhete):
    for s in cinema:
        if s[2]==filme:
          s[1] =s[1]+ nbilhete 
          print(f"Bilhetes vendidos com sucesso.\n Lugares Disponíveis:{lugaresdisponiveis(cinema,filme)}.")

def menu():
    print("Menu:\n 1-Criar Sala \n 2-Remover Sala \n 3-Listar Salas \n 4-Consultar salas\n 5-Lugares disponíveis \n 6- Vender bilhetes \n 0-Sair")
    op=int(input("Qual a opção do menu deseja selecionar?"))
    return op

op=menu()
while op !=0:
    if op==1:
        criarsala(cinema)
    elif op==2:
        if not cinema:
            print("Não existe salas no cinema para remover ")
        else:
            removersalas(cinema)
    elif op==3:
        if not cinema:
            print("Não é possível listar salas não existentes")
        else:
            listarsalas(cinema)
    elif op==4:
        if not cinema:
            print("Cinema sem salas")
        else:
            print(cinema)
    elif op==5:
        if not cinema:
            print("Não tem salas")
        else:
            filme=input("Qual é o filme que procura?")
            filme=filme.capitalize()
            Nr=lugaresdisponiveis(cinema,filme)
            if Nr==False:
                print("Não existe esse filme no cinema :(")
            else:
                print(f"Temos {Nr} lugares disponíveis para o filme {filme} para escolheres!")
    elif op==6:
        filme=input("Qual é o filme que procura?")
        filme=filme.capitalize()
        if not cinema:
            print("Não tem este filme")
        else:
            nbilhetes=int(input(f"Quantos bilhetes vai desejar para ver o filme {filme}?"))
            if Nr>nbilhetes:
                print(f"Ok! Aqui estão os seus {nbilhetes} bilhetes para ver o seu filme. Aproveite!")
                Nr=Nr-nbilhetes
            else:
                print("Não será possivel comprar os bilhetes para esse filme pois não existe lugares disponiveis.")
    else:
        print("Essa opção está inválida")
    op=menu()
print("Espero que tenha gostado e até a próxima!")
