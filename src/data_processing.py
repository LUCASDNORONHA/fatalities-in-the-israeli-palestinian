"""Funções para carregar, validar e preparar os dados do projeto."""

from pathlib import Path

import pandas as pd


ROOT_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = ROOT_DIR / "data" / "raw" / "fatalities_isr_pse_conflict_2000_to_2023.csv"
PROCESSED_DATA_PATH = ROOT_DIR / "data" / "processed" / "fatalities_preparadas.csv"

EXPECTED_COLUMNS = {
    "name", "date_of_event", "age", "citizenship", "event_location",
    "event_location_district", "event_location_region", "date_of_death",
    "gender", "took_part_in_the_hostilities", "place_of_residence",
    "place_of_residence_district", "type_of_injury", "ammunition", "killed_by", "notes",
}

AGE_BINS = [0, 14, 24, 34, 44, 54, 64, 150]
AGE_LABELS = ["0–14", "15–24", "25–34", "35–44", "45–54", "55–64", "65+"]


def carregar_dados(caminho: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Carrega o arquivo bruto e verifica se suas colunas são as esperadas."""
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo de dados não encontrado: {caminho}")

    dados = pd.read_csv(caminho)
    colunas_ausentes = EXPECTED_COLUMNS.difference(dados.columns)
    if colunas_ausentes:
        raise ValueError(f"Colunas ausentes no arquivo: {sorted(colunas_ausentes)}")
    return dados


def preparar_dados(dados_brutos: pd.DataFrame) -> pd.DataFrame:
    """Padroniza tipos e torna ausências explícitas sem imputar valores."""
    dados = dados_brutos.copy()
    dados["date_of_event"] = pd.to_datetime(dados["date_of_event"], errors="coerce")
    dados["date_of_death"] = pd.to_datetime(dados["date_of_death"], errors="coerce")
    dados["age"] = pd.to_numeric(dados["age"], errors="coerce")

    for coluna in [
        "gender", "took_part_in_the_hostilities", "type_of_injury", "ammunition",
        "place_of_residence", "place_of_residence_district",
    ]:
        dados[coluna] = dados[coluna].fillna("Desconhecido")

    dados["ano_evento"] = dados["date_of_event"].dt.year
    dados["ano_obito"] = dados["date_of_death"].dt.year
    dados["faixa_etaria"] = pd.cut(
        dados["age"], bins=AGE_BINS, labels=AGE_LABELS, include_lowest=True
    )
    dados["dias_ate_obito"] = (dados["date_of_death"] - dados["date_of_event"]).dt.days
    return dados


def salvar_dados_processados(dados: pd.DataFrame, caminho: Path = PROCESSED_DATA_PATH) -> Path:
    """Salva os dados preparados para consumo pelo notebook de análise."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    dados.to_csv(caminho, index=False)
    return caminho


def relatorio_qualidade(dados: pd.DataFrame) -> pd.DataFrame:
    """Retorna completude e tipo das colunas para auditoria do pré-processamento."""
    return pd.DataFrame({
        "coluna": dados.columns,
        "tipo": dados.dtypes.astype(str).values,
        "valores_ausentes": dados.isna().sum().values,
        "percentual_ausente": (dados.isna().mean().mul(100).round(2)).values,
    }).sort_values("percentual_ausente", ascending=False)
