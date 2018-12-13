**Resumo:** escolhendo de forma arbitrária um filtro para ser a base do experimento, avaliouse pares de filtros (o escolhido + outro da lista) e avaliou-se se os resultados de classificação melhoraram ou piorarm.
Foi usado para o teste um dataset de 128 imagens das categoria "buildings" e "animals", com 70% para treinamento, e 30% para validação. Também foi escolhido um Tree Classifier de forma arbitrária.

**O experimento:** O experimento teve 10 etapas. O filtro base escolhido foi o 'ColorLayoutFilter', o classificador escolhido foi o 'J48'

Primeira: O dataset foi classificado somente com o ColorLayoutFilter. Resultados obtidos: 
- 50% de classificações corretas

Segunda: ColorLayoutFilter e EdgeHistogramfilter. Resultados obtidos:
- 57.8% de classificações corretas
- Melhora de 7.8%
- Avaliação: ?

Terceira: ColorLayoutFilter e FCTHFilter. Resultados obtidos:
- 63.1% de classificações corretas
- Melhora de 13.1%
- Avaliação: Deve ser usado

Quarto: ColorLayoutFilter e FuzzyOpponentHistogramFilter. Resultados obtidos:
- 63.1% de classificações corretas
- Melhora de 13.1%
- Avaliação: Deve ser usado

Quinto: ColorLayoutFilter e GaborFilter. Resultados obtidos:
- 50% de classificações corretas
- Não interfere no resultado
- Avaliação: A principio não deve ser usado - mas é um candidato para eventuais testes futuros

Sexto: ColorLayoutFilter e JpegCoefficientFilter. Resultados obtidos:
- 76.3% de classificações corretas
- Melhora de 16.3%
- Avaliação: Deve ser usado

Sétimo: ColorLayoutFilter e PHOGFilter. Resultados obtidos:
- 68.4% de classificações corretas
- Melhora de 18.4%
- Avaliação: ?

Oitavo: ColorLayoutFilter e SimpleColorHistogramFilter. Resultados obtidos:
- 52.6% de classificações corretas
- Melhora de 2.6%
- Avaliação: Deve ser usado

Nono: ColorLayoutFilter e AutoColorCorrelogramFilter. Resultados obtidos:
- 63.1% de classificações corretas
- Melhora de 13.1%
- Avaliação: Deve ser usado

Décimo: ColorLayoutFilter e BinaryPatternsPyramidFilter. Resultados obtidos:
- 84.2% de classificações corretas
- Melhora de 34.2%
- Avaliação: Deve ser usado




