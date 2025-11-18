# Relatório do TPC4-Aplicação de gestão de um cinema
## Data:07-10-25
## Autor: Andreia Beatriz Barroso Ferreira A107234
## Resumo:
Neste tpc criei uma aplicação em que conseguimos gerir um cinema, suas salas onde passam diversos filmes, manipular a gestão dos lugares disponiveis como também os bilhetes disponiveis nujm centro comercial.
Considerei a seguinte sugestão para o modelo dos cinemas:
  ```
Cinema = [Sala]
Sala = [nlugares, Vendidos, filme]
nlugares = Int
filme = String 
Vendidos = [Int]
```
Além disso, definimos as seguintes funções que o professor sugeria na aula prática para conseguir fazer com que a aplicação funcionasse.