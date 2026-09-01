Descoberta 1
A análise da variável de custos revela que a distribuição dos dados não ocorre de maneira uniforme, apresentando uma forte concentração em faixas de menor valor. Embora a média registrada seja de 13270,42, a mediana encontra-se em um patamar bem inferior, fixada em 9382,03. Esse distanciamento entre as duas métricas indica claramente que um pequeno grupo de valores muito altos está puxando o resultado médio para cima, o que pode distorcer a interpretação do cenário financeiro caso a avaliação se baseie apenas na média de forma isolada.

Esse comportamento assimétrico fica evidente ao observarmos a representação gráfica, onde a maior parte dos registros se agrupa no início do eixo, formando uma longa cauda à direita no histograma devido às despesas excepcionalmente maiores. Consequentemente, a variabilidade dos dados torna-se bastante expressiva. O coeficiente de variação atingiu 91,26%, apontando uma dispersão altíssima em relação à própria média. Além disso, a aplicação do método do Intervalo Interquartil (IQR) reforçou essa característica ao identificar 139 outliers, que correspondem justamente a esses custos atípicos e elevados.

Conclui-se, portanto, que a maior parte dos registros está concentrada em despesas baixas e intermediárias. Já os valores extremos, embora representem uma parcela menor da base, exercem forte influência sobre a média e aumentam de forma significativa a dispersão geral dos custos analisados.

Média: 13270,42
Mediana: 9382,03
Desvio padrão: 12110,01
Coeficiente de variação: 91,26%
Valores atípicos (outliers): 139
Coeficiente de assimetria de Pearson: 0,96
Apoio visual: Histograma e Boxplot da variável Custos


Descoberta 2 
Ao investigar a relação entre a idade e os custos, a análise estatística apontou uma tendência de crescimento conjunto, embora com baixa intensidade. O coeficiente de correlação de Pearson resultou em 0,2990, indicando que de forma geral, os custos tendem a subir à medida que a idade avança. Contudo, por se tratar de um valor distante de 1, essa relação linear é considerada fraca. Esse comportamento reflete-se visualmente no diagrama de dispersão, onde a reta de regressão exibe uma inclinação ascendente, mas os pontos de dados permanecem bastante espalhados ao seu redor.

Para quantificar essa dinâmica, a regressão linear gerou o modelo expresso pela equação Y = 3165,89 + 257,72X. Na prática, o coeficiente aponta que, para cada ano adicional de idade, há um incremento projetado de aproximadamente 257,72 nos custos. Apesar dessa tendência de alta, o coeficiente de determinação (R²) obtido foi de apenas 0,0894. Isso demonstra que a idade consegue explicar menos de 9% de toda a variação dos custos presente na base de dados, limitando fortemente a capacidade preditiva do modelo se utilizado de forma isolada.

O ponto mais importante dessa análise é que, embora exista uma associação positiva entre idade e custos, a idade isoladamente não consegue explicar a maior parte das diferenças observadas na base. Esse resultado é relevante porque uma análise superficial poderia levar à impressão de que o aumento da idade seria suficiente para explicar o crescimento dos custos, quando o próprio R² mostra que essa relação representa apenas uma pequena parcela da variação total. Dessa forma, considerar apenas essa tendência poderia levar a uma interpretação incompleta dos dados. Além disso, a correlação observada indica apenas uma associação entre as variáveis e não estabelece uma relação de causalidade, o que sugere que outros fatores também precisam ser considerados para compreender melhor as diferenças de custos.

Descoberta 3
A comparação entre fumantes e não fumantes revelou uma das discrepâncias mais marcantes de toda a análise. Embora os fumantes representem uma minoria na base de dados, totalizando 274 registros (20,48%), contra 1.064 não fumantes (79,52%), esse grupo apresentou um custo médio de 32050,23. Esse montante contrasta drasticamente com a média de 8.434,27 observada entre o grupo que não possui o hábito de fumar.

Essa diferença substancial fica visualmente explícita no gráfico de barras, evidenciando que o custo médio entre os fumantes é quase quatro vezes maior. Trata-se de um diferença muito mais pronunciado sobre os valores do que as tendências observadas anteriormente nas análises isoladas de variáveis como idade ou IMC.

Portanto, a condição de fumante apresenta uma forte associação com custos mais elevados. No entanto, mantendo o rigor estatístico das análises de correlação, não é possível atestar causalidade direta baseando-se unicamente neste cruzamento, visto que outras variáveis podem atuar em conjunto com o tabagismo. O que se pode concluir com segurança é que a divisão por essa categoria expõe uma diferença marcante na base, consolidando o hábito de fumar como uma variável relevante para a compreensão do comportamento dos custos.

Resumo dos Indicadores
Custo médio dos fumantes: 32050,23
Custo médio dos não fumantes: 8434,27
Proporção de fumantes: 274 registros (20,48%)
Proporção de não fumantes: 1.064 registros (79,52%)
Apoio visual: Gráfico de barras comparativo do custo médio entre as categorias de fumantes e não fumantes.