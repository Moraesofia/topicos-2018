# topicos-2018

- Resultados dos experimentos relacionados ao trabalho final da disciplina Tópicos em Engenharia de Software 2018-2.
O objetivo do artigo foi de encontrar o melhor modelo possível para o probela de classificação de imagens por sua qualidada estética utilizando a ferramenta WEKA (https://www.cs.waikato.ac.nz/ml/weka/) e o pacote imageFilters (https://github.com/mmayo888/ImageFilter).

- Os datasets utilizados podem ser encontrados no site: https://www.figure-eight.com/data-for-everyone/ com os nomes:
  - How beautiful is this image? (Part 2: Buildings and Architecture); e
  - How beautiful is this image? (Part 3: Animals).

- Comando "convert" Linux para conversão do tamanho das imagens:
```ruby
convert '*.jpg[256x]' -set filename:base "%[base]" "%[filename:base].jpg"
```
-------------------------
Sofia Moraes

Engenharia de Software

Instituto de Informárica - UFG

2018-12-13
