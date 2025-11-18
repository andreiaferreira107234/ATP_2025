op=(-1)
lista=[]

import random

def menu ():
    print("Bem vindo!Selecione um modo:\n1)Criar lista\n2)Ler lista\n3)Somar lista\n4)Média da lista\n5)Procurar o maior elmento da lista\n6)Procurar o menor elemento\n7)Verificar se está na ordem crescente\n8)Verificar se está na ordem decrescente\n9)Procurar elemento da lista e indicar a posição\n0)Sair")
    return
def criarlista():
    lista=[]
    for i in range(5):
        n=random.randrange(1,101)
        lista.append(n)
    return lista

def lerlista():
    lista=[]
    for i in range(5):
        n=int(input(f"Pode introduzir o {i+1} número que esteja na lista"))
        lista.append(n)
    return lista

def somalista(lista):
    soma=0
    for i in lista:
        soma=soma + i
    return soma

def medialista(lista):
    for i in lista:
        media=somalista(lista)/len(lista) 
        return media
    
def pmaior(lista):
    i=0
    maior=0
    while i in lista and i<len(lista)-1:
        num=lista[i]
        i+=1
        if num>maior:
            maior=num
    return pmaior

def pmenor(lista):
    i=0
    menor=0
    while i in lista and i<len(lista)-1:
        num=lista[i]
        i+=1
        if num<menor:
            menor=num
    return pmenor

def ordenadacrescente(lista):
    ordenadacrescente="sim"
    i=0
    while ordenadacrescente and i<len(lista)-1:
        if lista[i]>lista[i+1]:
            ordenadacrescente="Não"
        i+=1                              #é igual a i=i+1
    return ordenadacrescente

def ordenadadecrescente(lista):
    ordenadadecrescente="Sim"
    i=0
    while ordenadadecrescente and i<len(lista)-1:
        if lista[i]<lista[i+1]:
            ordenadadecrescente="Não"
        i+=1
    return ordenadadecrescente

def procurar(lista,n):
    for i in range(len(lista)):
        if n==lista[i]:
         return i
    return -1


menu()
op=int(input("Introduza a sua opção de modo"))


while op!=0:
    if op==1:
        lista=criarlista()
        print(lista)
    elif op==2:
        lista=lerlista()
        print(lista)
    
    elif op==3:
        if not lista:
            print("Não existe lista")
        else:
            soma=somalista(lista)
            print(soma)
    elif op==4:
        if not lista:
            print("Não existe lista")
        else:
            media=medialista(lista)
            print(media)
    elif op==5:
        if not lista:
            print("Não existe lista")
        else:
            print(f"O maior da lista é", max(lista))
    elif op==6:
        if not lista:
            print("Não existe lista")
        else:
            print(f"O menor da lista é", min(lista))
    elif op==7:
        if not lista:
            print("Não existe lista")
        else:
            crescente=ordenadacrescente(lista)
            print(crescente)
    elif op==8:
        if not lista:
            print("Não existe lista")
        else:
            decrescente=ordenadadecrescente(lista)
            print(decrescente)
    elif op==9:
        if not lista:
            print("Não existe lista")
        else:
            n=int(input(" Introduza o número que quer encontrar na lista"))
            p=procurar(lista,n)
            if p==-1:
                print("Esse número não se encontra na lista")
            else: 
                print(f"O número {n} está na posição {p+1} da lista")
    else:
        print("Opção inválida")
    menu()
    op=int(input("Introduza a sua opção de modo"))

print(f"A lista final é {lista}.Volte sempre!")

     



 
     
 