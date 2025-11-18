#Gestão de alunos
#aluno=(nome,id,[notaTpc,notaProjeto,notaTeste])
#turma=[alunos]
#Exemplos de alunos da minha escolhina:
#Aluna1=(Ariana Grande,123456,[12,19,20])
#Aluno2=(Adrien Agreste,234567,[20,19,20])
#Aluna3=(Maria Vaicomtodas,222222,[12,19,20])
#Aluno4=(Alice Vinhoverde,233333,[20,19,20])
#Aluna5=(Andreia Bestbuy,155555,[12,19,20])

def criarturma():
    turma=[]
    print("Turma criada com sucesso.Muito bem!")
    return turma

def inseriralunonaturma(turma):
    nome=input("Qual é o nome do aluno que deseja colocar na turma?")
    id=input("Qual é o número de identificação do aluno?")
    for x in turma:
        while id in x:
         print("Já temos esse aluno na turma")
         id=int(input("Introduza outro número de identificação"))
    notaTPC=float(input("Introduza a nota do trabalho de casa do/a aluno/a:"))
    while notaTPC<0 and notaTPC>20:
       print("Não é possivel registar essa nota, é inválida")
    notaProjeto=float(input("Introduza a nota do projeto do/a aluno/a :"))
    while notaProjeto<0 and notaProjeto>20:
       print("Não é possivel registar essa nota, é inválida")
    notaTeste=float(input("Introduza a nota do teste do/a aluno/a:"))
    while notaTeste<0 and notaTeste>20:
       print("Não é possivel registar essa nota, é inválida")
    aluno=(nome,id,[notaTPC,notaProjeto,notaTeste])
    turma.append(aluno)
    return

def listarturma(turma):
   print("A lista dos alunos:")
   for x in turma:
      print(turma)


def consultarturma(turma):
   id=input("Qual é o número de identificação do aluno?")
   y=False
   for x in turma:
        if x[1]==id:
           print(x)
           y=True
        else:
           print("Não temos um aluno com esse número de identicação nas turmas")
           y=False

def linha(aluno):
    nome, id, notas = aluno
    return f"{nome},{id},{notas[0]},{notas[1]},{notas[2]}\n"


def guardarTurma(turma, fnome):
    file = open(fnome, "w")   
    for aluno in turma:        
        file.write(linha(aluno))  
    file.close()


def carregar_turma():
    nome_arquivo = input("Nome do arquivo para carregar a turma (ex: turma.txt): ")
    global turma
    try:
        with open(nome_arquivo, 'r') as file:
            turma = []
            for linha in file:
                informaçoes = linha.strip().split(',')
                if len(informaçoes) == 5:
                    nome, id, notaTPC, notaProj, notaTeste = informaçoes
                    aluno = (nome, id, [float(notaTPC), float(notaProj), float(notaTeste)])
                    turma.append(aluno)
        print(f"Turma carregada do arquivo {nome_arquivo}.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except ValueError:
        print("Erro ao processar o arquivo. Verifique o formato dos dados.")

def menu_turma():
    print("Bem vindo ao menu! Temos as seguintes opções:\n 1-Criar turma \n 2-Inserir aluno 3-Listar Turmas \n 4-Consultar uma turma através do id do aluno \n 5-Guardar turma \n 6-Carregar Turma \n 0-Sair")
    op=int(input("Qual é a opção que deseja?"))
    return op

op=menu_turma()
while op!=0:
    if op==1:
        turma=criarturma()
    elif op==2:
        inseriralunonaturma(turma)
        print("O aluno foi inserido na turma!")
        res=input("Deseja inserir mais um aluno? Se sim, escreva ""s""")
        if res=="s":
            inseriralunonaturma(turma)
    elif op==3:
        if not turma:
            print("Não existe uma turma")
        else:
            listarturma(turma)
    elif op==4:
        if not turma:
            print("Não existe uma turma")
        else:
            consultarturma(turma)
    elif op==5:
        if not turma:
            print("Não existe uma turma")
        else:
            guardarTurma(turma,"turma.txt")
            print("A turma foi guardada num ficheiro")
    elif op==6:
        if not turma:
            print("Não existe uma turma")
        else:
            carregar_turma()
    op=menu_turma()
print("Obrigada e volte sempre")