**Resumo:** Todos os filtros que passaram na primeira parte do experimento serão testados nessa segunda etapa. O princípio é adicionar os filtros um a um e efetuar a classificação. Se a partir do segundo input, o filtro não apresentar uma melhora na classificação ele será retirado. Será seguida a mesma sequência de aplicação de filtros da primeira etapa do experimento. Foi usado para o teste um dataset de 1024 imagens da categoria "buildings" e "animals", com 70% para treinamento, e 30% para validação. Também foi escolhido um Tree Classifier de forma arbitrária.

**O experimento:** O primeiro filtro escolhido foi o 'ColorLayoutFilter', o classificador escolhido foi o 'J48'. 
Etapas:

Primeira: O dataset foi classificado somente com o ColorLayoutFilter. Resultados obtidos: 
- 57.6% de classificações corretas

Segunda: ColorLayoutFilter e EdgeHistogramFilter.
- 54.3%
- Houve piora. Filtro será descartado

Terceiro: ColorLayoutFilter e FCTHFilter.
- 58.3%
- Houve melhora, filtro será mantido

Quarto: ColorLayoutFilter, FCTHFilter e FuzzyOpponentHistogramFilter.
- 56.0%
- Houve piora, filtro será removido

Quinto: ColorLayoutFilter, FCTHFilter e JpegCoefficientFilter.
- 60.2%
- Houve melhora, filtro será mantido

Sexto: ColorLayoutFilter, FCTHFilter, JpegCoefficientFilter e PHOGFilter.
- 61.5%
- Houve melhora, filtro será mantido

Sétimo: ColorLayoutFilter, FCTHFilter, JpegCoefficientFilter, PHOGFilter e SimpleColorHistogramFilter.
- 57.9%
- Houve piora, filtro será removido

Oitavo: ColorLayoutFilter, FCTHFilter, JpegCoefficientFilter, PHOGFilter e AutoColorCorrelogramFilter.
- 57.9%
- Houve piora, filtro será removido

Nono: ColorLayoutFilter, FCTHFilter, JpegCoefficientFilter, PHOGFilter e BinaryPatternsPyramidFilter.
- 57.3%
- Houve piora, filtro será removido

Décimo (EXTRA) - Todos os filtros
- 60.9%

RESULTADOS
- Melhor combinação: ColorLayoutFilter, FCTHFilter, JpegCoefficientFilter e PHOGFilter.
- 61.5635%

