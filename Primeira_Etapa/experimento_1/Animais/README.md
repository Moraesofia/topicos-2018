**Resumo:** escolhendo de forma arbitrária um filtro para ser a base do experimento, avaliou-se pares de filtros (o escolhido + outro da lista) e avaliou-se se os resultados de classificação melhoraram ou piorarm.
Foi usado para o teste um dataset de 64 imagens da categoria "animals", com 70% para treinamento, e 30% para validação. Também foi escolhido um Tree Classifier de forma arbitrária.

**O experimento:** O experimento teve 10 etapas. O filtro base escolhido foi o 'ColorLayoutFilter', o classificador escolhido foi o 'J48'

Primeira: O dataset foi classificado somente com o ColorLayoutFilter. Resultados obtidos: 
- 42.1% de classificações corretas

Segunda: ColorLayoutFilter e EdgeHistogramfilter. Resultados obtidos:
- 36.8% de classificações corretas
- Piora de 5.3% (pequena piora)
- Avaliação: Não deve ser usado

Terceira: ColorLayoutFilter e FCTHFilter. Resultados obtidos:
- 47.3% de classificações corretas
- Melhora de 5.2% (pequena melhora)
- Avaliação: Deve ser usado

Quarto: ColorLayoutFilter e FuzzyOpponentHistogramFilter. Resultados obtidos:
- 31.5% de classificações corretas
- Piora de 10% (grande piora)
- Avaliação: Não deve ser usado

Quinto: ColorLayoutFilter e GaborFilter. Resultados obtidos:
- 42.1% de classificações corretas
- Não interfere no resultado
- Avaliação: A principio não deve ser usado - mas é um candidato para eventuais testes futuros

Sexto: ColorLayoutFilter e JpegCoefficientFilter. Resultados obtidos:
- 63.1% de classificações corretas
- Melhora de 21% (grande melhora)
- Avaliação: Deve ser usado

Sétimo: ColorLayoutFilter e PHOGFilter. Resultados obtidos:
- 26.3% de classificações corretas
- Piora de 18.8% (grande piora)
- Avaliação: Não deve ser usado

Oitavo: ColorLayoutFilter e SimpleColorHistogramFilter. Resultados obtidos:
- 36.8% de classificações corretas
- Piora de 5.3% (pequena piora)
- Avaliação: Não deve ser usado

Nono: ColorLayoutFilter e AutoColorCorrelogramFilter. Resultados obtidos:
- 42.1% de classificações corretas
- Não interfere no resultado
- Avaliação: A principio não deve ser usado - mas é um candidato para eventuais testes futuros

Décimo: ColorLayoutFilter e BinaryPatternsPyramidFilter. Resultados obtidos:
- 68.4% de classificações corretas
- Melhora de 26.3% (grande melhora)
- Avaliação: Deve ser usado




