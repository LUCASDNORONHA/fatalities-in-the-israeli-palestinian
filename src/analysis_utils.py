"""Agregações e gráficos reutilizáveis para a análise exploratória."""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def tabela_frequencia(dados: pd.DataFrame, coluna: str) -> pd.DataFrame:
    """Calcula contagem e participação percentual de uma variável categórica."""
    frequencias = dados[coluna].value_counts(dropna=False).rename_axis(coluna).reset_index(name="fatalidades")
    frequencias["percentual"] = (frequencias["fatalidades"] / len(dados) * 100).round(2)
    return frequencias


def fatalidades_por_ano(dados: pd.DataFrame) -> pd.DataFrame:
    """Agrega registros pelo ano do óbito, excluindo datas indisponíveis."""
    return (
        dados.dropna(subset=["ano_obito"])
        .groupby("ano_obito")
        .size()
        .rename("fatalidades")
        .reset_index()
    )


def grafico_barras(tabela: pd.DataFrame, categoria: str, titulo: str, rotacao: int = 25):
    """Cria um gráfico de barras consistente para as tabelas de frequência."""
    sns.set_theme(style="whitegrid", context="notebook")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(data=tabela, x=categoria, y="fatalidades", color="#9e2a2b", ax=ax)
    ax.set(title=titulo, xlabel="", ylabel="Número de fatalidades")
    ax.tick_params(axis="x", rotation=rotacao)
    for container in ax.containers:
        ax.bar_label(container, padding=3, fontsize=9)
    fig.tight_layout()
    return fig, ax


def grafico_linha_anual(tabela: pd.DataFrame):
    """Cria uma série temporal de fatalidades por ano de óbito."""
    sns.set_theme(style="whitegrid", context="notebook")
    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(tabela["ano_obito"], tabela["fatalidades"], marker="o", color="#9e2a2b", linewidth=2)
    ax.set(title="Fatalidades por ano de óbito", xlabel="Ano", ylabel="Número de fatalidades")
    ax.set_xticks(tabela["ano_obito"].iloc[::2])
    fig.tight_layout()
    return fig, ax
