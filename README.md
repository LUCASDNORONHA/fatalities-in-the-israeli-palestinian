# Análise de Fatalidades no Conflito Israelense-Palestino

Projeto de análise exploratória de dados, em Python, sobre registros individuais de fatalidades entre 2000 e setembro de 2023.

## Estrutura

```text
data/
├── raw/                         # Fonte original em CSV
└── processed/                   # Base preparada (gerada localmente)
notebooks/
├── 01_preprocessamento.ipynb    # Limpeza, validação e criação de variáveis
└── 02_analise_exploratoria.ipynb# Perguntas, tabelas e visualizações
src/
├── data_processing.py           # Carregamento e preparação dos dados
└── analysis_utils.py            # Tabelas e gráficos reutilizáveis
```

## Executar com uv

```bash
uv sync
uv run jupyter lab
```

Execute primeiro `notebooks/01_preprocessamento.ipynb` e, em seguida, `notebooks/02_analise_exploratoria.ipynb`.

Também é possível reproduzir o pré-processamento sem abrir o Jupyter:

```bash
uv run python -c "from src.data_processing import carregar_dados, preparar_dados, salvar_dados_processados; salvar_dados_processados(preparar_dados(carregar_dados()))"
```

## Metodologia

- O arquivo bruto é preservado em `data/raw/`.
- Dados ausentes não recebem valores presumidos: campos categóricos são marcados como `Desconhecido`, e a idade ausente permanece ausente.
- A análise temporal utiliza o ano do óbito; a data do evento continua disponível para comparação.
- O projeto é descritivo e não estabelece causalidade, responsabilidade legal ou completude da base.

Veja [PROJECT_GUIDE.md](PROJECT_GUIDE.md) para escopo, limitações e fonte dos dados.
