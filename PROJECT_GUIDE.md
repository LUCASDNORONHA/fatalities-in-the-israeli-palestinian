# Guia do projeto

## Objetivo

Este repositório apresenta uma análise exploratória reproduzível de **11.124** registros de fatalidades no conflito israelense-palestino. A fonte cobre eventos de **2 de outubro de 2000** até **24 de setembro de 2023**.

O trabalho descreve os registros fornecidos. Ele não estabelece causalidade, responsabilidade legal ou completude da fonte original.

## Fluxo de trabalho

1. `01_preprocessamento.ipynb` valida a fonte, padroniza tipos, trata ausências de forma explícita e salva `data/processed/fatalities_preparadas.csv`.
2. `02_analise_exploratoria.ipynb` usa exclusivamente essa base preparada para produzir tabelas e gráficos.
3. As funções de leitura, preparação e visualização ficam em `src/`, fora dos notebooks, para serem reutilizáveis e testáveis.

## Decisões metodológicas

- Datas de evento e de óbito são mantidas separadas. Há **910** registros em que o óbito é posterior ao evento.
- A idade ausente não é substituída pela média; ela é excluída somente das análises que dependem da idade.
- Ausências em campos categóricos são rotuladas como `Desconhecido`, sem inferir gênero, local de residência ou participação em hostilidades.
- Os gráficos temporais usam o ano do óbito.

## Limitações

- A base é um recorte histórico e não recebe atualização automática.
- As categorias, atribuições e ausências refletem práticas e definições da fonte dos dados.
- As contagens podem ser afetadas por cobertura, classificação e revisões da fonte.
- A terminologia do conflito é contestada; atributos devem ser lidos como valores registrados na base, não como verificação independente.

## Fonte

[Kaggle — Fatalities in the Israeli & Palestinian](https://www.kaggle.com/datasets/willianoliveiragibin/fatalities-in-the-israeli-palestinian)

Consulte os termos da fonte antes de redistribuir os dados ou artefatos derivados.
