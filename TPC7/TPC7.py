#TPC8:Teste de aferição

##Tpc 1:Especifique as seguintes listas em compreensão:

###a)
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  
ncomuns = [n for n in lista1 + lista2 if (n in lista1) != (n in lista2)]

###c)
lista = ['anaconda', 'burro', 'cavalo', 'macaco']
listaRes = [(i+1, lista[i]) for i in range(len(lista))]
###b)
texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""
lista = [n for n in texto.split(" ") if len(n)>3]

##tpc 2-À semelhança do que foi feito nas aulas, realize as seguintes tarefas
###a)
def strCount(s, subs):
    cont=0
    n=len(subs) 
    for i in range(len(s)-n+1):
        if s[i:i+n]==subs:
            cont=cont+1 #ou cont+=1
            i+=n-1
    return cont
strCount("catcowcat", "cat") # --> 2
print((strCount("catcowcat", "cat")),(strCount("catcowcat", "cow")),(strCount("catcowcat", "dog")))
###b)
def produtoM3(lista):
    if len(lista)<3:
        print("Não é possivel pois tem de ter no minimo três números positivos na lista")
    else:
     menores=sorted(lista)[:3]
     produto_menores=menores[0]*menores[1]*menores[2]
    return produto_menores 
print(produtoM3([12,3,7,10,12,8,9]))
###c)
def reduxInt(n):
    if n==0:
        soma=0
    else:
        soma=1+(n -1)%9
    return soma
print(reduxInt(38))
###d)
def myIndexOf(s1, s2):
    i = 0
    resultado = -1
    while i <= len(s1) - len(s2):
        if s1[i:i+len(s2)] == s2:
            resultado = i
            i += 1
        else:
            i += 1
    return resultado
print(myIndexOf("Hoje está um belo dia de sol!", "chuva"))

##Tpc 3-A rede social
###a)
def quantosPost(redeSocial):
    return len(redeSocial)
###b)
def postsAutor(redeSocial, autor):
    res= []
    for post in redeSocial:
        if autor == post["autor"]:
            res.append(post)
    return res
###c)
def autores(redeSocial):
    lista=[]
    for post in redeSocial:
        if "autor" in post:
            lista.append(post["autor"])
    return  lista
###d)
def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    id = f"p{len(redeSocial)+1}"
    novo_post= {
        'id':id,
        'conteudo':conteudo,
        'autor':autor,
        'dataCriacao':dataCriacao,
        'comentarios':comentarios
    }
    redeSocial.append(novo_post)
    return redeSocial
###e)
def remPost(redeSocial, id):
   for post in redeSocial:
    post['id']==id
    redeSocial.remove(post)
    return redeSocial
###f)
def postsPorAutor(redeSocial):
    n = {}
    for post in redeSocial:
        autor = post.get("autor")
        if autor in n:
            n[autor] += 1
        else:
            n[autor] = 1
    return n
###g)
def comentadoPor(redeSocial, autor):
    res=[]
    for n in redeSocial: 
        for i in n['comentarios']:
            if i['autor'] == autor:
                res.append(n)
    return res



