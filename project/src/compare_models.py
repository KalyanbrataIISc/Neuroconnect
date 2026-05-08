"""Model-comparison placeholders for real and synthetic network metrics."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

import pandas as pd


def normalized_metric_distance(
    real_metrics: dict[str, Any],
    model_metrics: dict[str, Any],
    selected_metrics: Iterable[str],
) -> float:
    """Compute a normalized distance between real and model metric values.

    Args:
        real_metrics: Metrics computed on the empirical graph.
        model_metrics: Metrics computed on a synthetic model graph.
        selected_metrics: Metric keys to include in the comparison.

    Returns:
        ``0.0`` as a placeholder distance.
    """
    _ = real_metrics, model_metrics, list(selected_metrics)
    return 0.0


def rank_models(
    real_metrics: dict[str, Any],
    model_metrics_dict: dict[str, dict[str, Any]],
) -> pd.DataFrame:
    """Rank synthetic models by similarity to the empirical graph.

    Args:
        real_metrics: Metrics computed on the empirical graph.
        model_metrics_dict: Mapping of model name to computed metrics.

    Returns:
        Empty ranking DataFrame placeholder with expected columns.
    """
    _ = real_metrics, model_metrics_dict
    return pd.DataFrame(columns=["model", "distance", "rank"])


def save_comparison_tables(results: pd.DataFrame, output_dir: str | Path) -> Path:
    """Save comparison tables to the results directory.

    Args:
        results: Comparison results table.
        output_dir: Directory where future tables should be written.

    Returns:
        Planned output path for the comparison table.
    """
    _ = results
    return Path(output_dir) / "model_comparison.csv"

