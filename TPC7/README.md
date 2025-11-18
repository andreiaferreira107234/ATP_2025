# Relatório do TPC7 - Teste de aferição
## Data:28-10-25
## Autor: Andreia Beatriz Barroso Ferreira A107234
## Resumo:

Neste tpc tivemos três "mini tpcs": tpc1 baseiava-se em especificar as listas pedidas em compressão;o tpc2 baseiava-se em realizar umas tarefas que játinham sido feitas em aula e o tpc3 baseiava-se em produzir diversas funçóes em volta de uma aplicação "Rede Social".
Em mais pormenor, o tpc3 tinha diversas funções como acrescentar posts novos como também remover, ver os posts que um autor tenha na rede social, etc.
O mecanismo usado era que a informação sobre uma rede social estava armazenada numa lista de dicionários.
Cada dicionário, correspondente a um _post_ e tem chaves id, conteudo, autor, dataCriacao e comentarios.
Por sua vez, comentarios é uma lista de dicionários com chaves "comentario" e "autor".
Assim, o utlizador tem a chance de gerir uma rede social através das funções criadas.